from __future__ import unicode_literals, print_function
import numpy as np
import matplotlib.pyplot as plt
import serial
import seaborn as sns
sns.set(font_scale=2)
s = serial.Serial('/dev/tty.usbserial-A1065Q8N')

def main():

	fig, ax = plt.subplots(1,1)

	t = np.arange(0,10,0.1)

	list_1 = np.zeros(100).tolist()

	lines_1, = ax.plot(t, list_1,'r--',label="1")

	list_2 = np.zeros(100).tolist()

	lines_2, = ax.plot(t, list_2,'b--',label="2")

	ax.set_ylim((200,820))

	ax.set_ylabel("val", size = 30)
	ax.set_xlabel("Time[s]" , size = 30)

	acc = s.readline().split(",",0)

	while True:
		t += 0.1
		acc = s.readline().split(",",0)

		acc_1 = float(acc[0])
		acc_2 = float(acc[1])

		list_1.pop(0)
		list_1.append(acc_1)

		list_2.pop(0)
		list_2.append(acc_2)

		plt.draw()

		lines_1.set_data(t, list_1)
		lines_2.set_data(t, list_2)

		ax.set_xlim((t.min(), t.max()))

		plt.pause(.0001)
		

if __name__ == '__main__':
    main()