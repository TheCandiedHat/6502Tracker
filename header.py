
from editor import testHeader

f = open("output.asm", 'w');
f.write("  .inesprg " + str(testHeader[0]));
f.write("  .ineschr " + str(testHeader[1]));
f.write("  .inesmap " + str(testHeader[2]));
f.write("  .inesmir " + str(testHeader[3]));
