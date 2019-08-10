import VMDGen
#
# regular = [
#     ['[', ' [ '],
#     [']', ' ] '],
#     ['(', ' ( '],
#     [')', ' ) '],
#     [':', ' : '],
#     [';', ' ; '],
#     [',', ' , '],
#     ['\t', ' '],
#     ['\n', ' '],
#     ['=', ' = '],
#     ['<=', ' <= ']
# ]
#
#
#
#
#
# def FileToList(PATH):
#     l = []
#     out = []
#     with open(PATH) as f:
#         l = f.read()
#         for i in range(len(regular)):
#             l = l.replace(regular[i][0], regular[i][1])
#     l = l.split(' ')
#     for i in range(len(l)):
#         if l[i] != '' and l[i] != ',' and l[i] != ';' and l[i] != ';' and l[i] != 'reg' and l[i] != 'wire' and l[i] != ':':
#             out.append(l[i])
#     print(out)
#     return out
#
#
# def ParserList(list):
#     global file, ListToPrint, portlist
#     global OpenModule, InputPort, OutputPort, NammeModule, ID, Portst, Portend, Hadr, Ladr, Wdthst, WdthH, Wdtend, InOutPort
#     OpenModule = 0
#     NammeModule = 0
#     InputPort = 0
#     OutputPort = 0
#     InOutPort = 0
#     ID = 0
#     Portst = 0
#     Portend = 0
#     Hadr = 0
#     Ladr = 0
#     Wdthst = 0
#     WdthH = 0
#     Wdtend = 0
#     portlist = []
#     ListToPrint = []
#     for i in range(len(list)):
#         if list[i] == 'module':
#             OpenModule = 1
#         elif portlist.count(list[i]):
#             index = portlist.index(list[i])
#             ListToPrint[index][2] = str(int(Hadr) + 1 - int(Ladr))
#             if (InputPort):
#                 dirvar = 'input'
#             elif (OutputPort):
#                 dirvar = 'output'
#             elif InOutPort:
#                 dirvar = 'inout'
#             else:
#                 dirvar = 'none'
#             ListToPrint[index][3] = dirvar
#         elif list[i] == 'endmodule':
#             OpenModule = 0
#             NammeModule = 0
#             InputPort = 0
#             OutputPort = 0
#             InOutPort = 0
#             ID = 0
#             Portst = 0
#             Portend = 0
#             Hadr = 0
#             Ladr = 0
#             Wdthst = 0
#             WdthH = 0
#             Wdtend = 0
#             PrintPORT(ListToPrint)
#             file.write("</module>\n")
#             file.close()
#             portlist = []
#             ListToPrint = []
#         elif OpenModule == 1 and NammeModule == 0:
#             NammeModule = 1
#             file = open(list[i] + '.vmd', 'w')
#             file.write("<module>\n")
#             file.write("<name>" + list[i] + "</name\n")
#         elif list[i] == '(' and Portend == 0:
#             Portst = 1
#             file.write("<body>\n")
#         elif list[i] == ')' and Portst == 1:
#             Portend = 1
#             file.write("</body>\n")
#         elif list[i] == ']' and Wdtend and Wdthst and WdthH:
#             Wdtend = 0
#             Wdthst = 0
#             WdthH = 0
#         elif Wdthst and WdthH:
#             Ladr = list[i]
#             Wdtend = 1
#         elif list[i] == '[':
#             Wdthst = 1
#         elif Wdthst:
#             Hadr = list[i]
#             WdthH = 1
#         elif list[i] == 'input':
#             InputPort = 1
#             OutputPort = 0
#             InOutPort = 0
#             Hadr = 0
#             Ladr = 0
#         elif list[i] == 'output':
#             InputPort = 0
#             OutputPort = 1
#             InOutPort = 0
#             Hadr = 0
#             Ladr = 0
#         elif list[i] == 'inout':
#             InputPort = 0
#             OutputPort = 0
#             InOutPort = 1
#             Hadr = 0
#             Ladr = 0
#         elif Portst == 1 and Portend == 0 and list[i] != 'input' and list[i] != 'output' and list[
#             i] != 'inout' and Wdthst != 1:
#             if (InputPort):
#                 dirvar = 'input'
#             elif (OutputPort):
#                 dirvar = 'output'
#             elif InOutPort:
#                 dirvar = 'inout'
#             else:
#                 dirvar = 'none'
#
#             ListToPrint.append([str(ID), list[i],  str(int(Hadr) + 1 - int(Ladr)), dirvar])
#             ID += 1
#             portlist.append(list[i])
#         else:
#             pass
#         print(list[i])
#         print(OpenModule, InputPort, OutputPort, InOutPort, NammeModule, ID, Portst, Portend, Hadr, Ladr, Wdthst, WdthH, Wdtend)
#         print(portlist)
#         print(ListToPrint)
#
#
# def PrintPORT(LST):
#     for i in range(len(LST)):
#         file.write("<port>\n\t<ID>" + LST[i][0] + "</ID>\n\t<nameport>" + LST[i][1] + "</nameport>\n\t<width>" + LST[i][2] + "</width>\n\t<direct>" + LST[i][3] + "</direct>\n</port>\n")

def main():
    test = VMDGen.VMDGEN('test.v')
    list = test.FileToList()
    test.ParserList(list)


if __name__ == '__main__':
    main()
