VMDGen_REGULAR = [
    ['[', ' [ '],
    [']', ' ] '],
    ['(', ' ( '],
    [')', ' ) '],
    [':', ' : '],
    [';', ' ; '],
    [',', ' , '],
    ['\t', ' '],
    ['\n', ' '],
    ['=', ' = '],
    ['<=', ' <= ']
]


class VMDGEN:

    def __init__(self, path):
        self.file = 'none'
        self.ListToPrint = []
        self.portlist = []
        self.OpenModule = 0
        self.InputPort = 0
        self.OutputPort = 0
        self.NammeModule = 0
        self.ID = 0
        self.Portst = 0
        self.Portend = 0
        self.Hadr = 0
        self.Ladr = 0
        self.Wdthst = 0
        self.WdthH = 0
        self.Wdtend = 0
        self.InOutPort = 0
        self.ModuleName = 'none'
        self.path = path

    def FileToList(self):
        out = []
        with open(self.path) as f:
            l = f.read()
            for i in range(len(VMDGen_REGULAR)):
                l = l.replace(VMDGen_REGULAR[i][0], VMDGen_REGULAR[i][1])
        l = l.split(' ')
        for i in range(len(l)):
            if l[i] != '' and l[i] != ',' and l[i] != ';' and l[i] != ';' and l[i] != 'reg' and l[i] != 'wire' and l[
                i] != ':':
                out.append(l[i])
        print(out)
        return out

    def ParserList(self, list):
        self.OpenModule = 0
        self.NammeModule = 'None'
        self.InputPort = 0
        self.OutputPort = 0
        self.InOutPort = 0
        self.ID = 0
        self.Portst = 0
        self.Portend = 0
        self.Hadr = 0
        self.Ladr = 0
        self.Wdthst = 0
        self.WdthH = 0
        self.Wdtend = 0
        self.portlist = []
        self.ListToPrint = []
        for i in range(len(list)):
            if list[i] == 'module':
                OpenModule = 1

            elif self.portlist.count(list[i]):
                index = self.portlist.index(list[i])
                self.ListToPrint[index][2] = str(int(self.Hadr) + 1 - int(self.Ladr))
                if self.InputPort:
                    dirvar = 'input'
                elif self.OutputPort:
                    dirvar = 'output'
                elif self.InOutPort:
                    dirvar = 'inout'
                else:
                    dirvar = 'none'
                self.ListToPrint[index][3] = dirvar

            elif list[i] == 'endmodule':
                self.OpenModule = 0
                self.NammeModule = 0
                self.InputPort = 0
                self.OutputPort = 0
                self.InOutPort = 0
                self.ID = 0
                self.Portst = 0
                self.Portend = 0
                self.Hadr = 0
                self.Ladr = 0
                self.Wdthst = 0
                self.WdthH = 0
                self.Wdtend = 0
                self.PrintPORT()
                self.portlist = []
                self.ListToPrint = []
            elif self.OpenModule == 1 and self.NammeModule == 0:
                self.NammeModule = 1
                self.ModuleName = list[i]

            elif list[i] == '(' and self.Portend == 0:
                self.Portst = 1


            elif list[i] == ')' and self.Portst == 1:
                self.Portend = 1

            elif list[i] == ']' and self.Wdtend and self.Wdthst and self.WdthH:
                self.Wdtend = 0
                self.Wdthst = 0
                self.WdthH = 0

            elif self.Wdthst and self.WdthH:
                self.Ladr = list[i]
                self.Wdtend = 1

            elif list[i] == '[':
                self.Wdthst = 1

            elif self.Wdthst:
                self.Hadr = list[i]
                self.WdthH = 1

            elif list[i] == 'input':
                self.InputPort = 1
                self.OutputPort = 0
                self.InOutPort = 0
                self.Hadr = 0
                self.Ladr = 0

            elif list[i] == 'output':
                self.InputPort = 0
                self.OutputPort = 1
                self.InOutPort = 0
                self.Hadr = 0
                self.Ladr = 0

            elif list[i] == 'inout':
                self.InputPort = 0
                self.OutputPort = 0
                self.InOutPort = 1
                self.Hadr = 0
                self.Ladr = 0

            elif self.Portst == 1 and self.Portend == 0 and list[i] != 'input' and list[i] != 'output' and list[
                i] != 'inout' and self.Wdthst != 1:
                if self.InputPort:
                    dirvar = 'input'
                elif self.OutputPort:
                    dirvar = 'output'
                elif self.InOutPort:
                    dirvar = 'inout'
                else:
                    dirvar = 'none'

                self.ListToPrint.append([str(self.ID), list[i], str(int(self.Hadr) + 1 - int(self.Ladr)), dirvar])
                self.ID += 1
                self.portlist.append(list[i])

            else:
                pass

            print(list[i])
            print(self.OpenModule, self.InputPort, self.OutputPort, self.InOutPort, self.NammeModule, self.ID, self.Portst, self.Portend, self.Hadr, self.Ladr, self.Wdthst,
                  self.WdthH, self.Wdtend)
            print(self.portlist)
            print(self.ListToPrint)

    def PrintPORT(self):
        file = open(self.OpenModule + '.vmd', 'w')
        file.write("<module>\n")
        file.write("<name>" + self.ModuleName + "</name\n")
        file.write("<body>\n")
        for i in range(len(self.ListToPrint)):
            file.write(
                "<port>\n\t<ID>" + self.ListToPrint[i][0] + "</ID>\n\t<nameport>" + self.ListToPrint[i][1] + "</nameport>\n\t<width>" + self.ListToPrint[i][
                    2] + "</width>\n\t<direct>" + self.ListToPrint[i][3] + "</direct>\n</port>\n")
        file.write("</body>\n")
        file.write("</module>\n")
        file.close()
