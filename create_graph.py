import subprocess
import matplotlib.pyplot as plt

x = []
y = []
for i in range(20,800,40):
    command = "./stencil "+ str(i)+ " " +str(i)
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    string = output.split("\n")[3]
    mflops = string.replace("#","").replace("=","").split()[1]
    x.append(i)
    y.append(float(mflops)/1000)
    print(".")

plt.plot(x,y, color='green')
plt.xlabel('STENCIL_SIZE_X = STENCIL_SIZE_Y')
plt.ylabel('gflops')
plt.title("Performance en gigaflops")
plt.savefig('performance.png')
