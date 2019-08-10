module Mymodule1
(
	input CLK, RESET,
	input [7:0] A,B,
	output	reg [ 7 : 0 ] C
);


endmodule

module Mymodule2( CLK, RESET, A, B,C );
input CLK, RESET;
input [7:0] A,B;
output	reg [ 7 : 0 ] C;

endmodule

module TEst1(CLK, RESET, A, B);
(CLK1, RESET1, A1, B1);
input CLK, RESET, A;
output B;
wire B;
reg B_fl;

always@(*)
    B_fl <= B;

assign B = (~B) && B_fl;

endmodule