from tkinter import *
from tkinter import messagebox
root = Tk()
index=0

def addrecord(event):
	global index
	file=open('sample.txt','a')
	file.write(entry1.get()+'\t'+entry2.get()+'\t'+entry3.get()+'\t'+entry4.get()+'\t'+entry5.get()+'\t'+entry6.get()+'\n')
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	messagebox.showinfo('Alert','Record added!')
	file.close()

def removerecord(event):
	file=open('sample.txt','r')
	lines=file.readlines()
	file.close()
	file=open('sample.txt','w')
	for line in lines:
		com=line.split()
		if com[0]!=entry1.get():
			file.write(line)
	messagebox.showinfo('Alert','Record deleted!')
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	file.close()

def searchrecord(event):
	file=open('sample.txt','r')
	lines=file.readlines()
	com=[]
	s=False
	for line in lines:
		com=line.split()
		if com[0]==entry1.get():
			messagebox.showinfo('Alert','Record found')
			s=True
			entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');

			entry1.insert(0,com[0]);entry2.insert(0,com[1]);entry3.insert(0,com[2]);entry4.insert(0,com[3]);entry5.insert(0,com[4]);entry6.insert(0,com[5]);
			break
		
	
	if s==False:
		messagebox.showinfo('Alert','Record not found')
	file.close()

def updaterecord(event):
	file=open('sample.txt','r')
	lines=file.readlines()
	file.close()
	file=open('sample.txt','w')
	for line in lines:
		com=line.split()
		if com[0]==entry1.get():
			file.write(entry1.get()+'\t'+entry2.get()+'\t'+entry3.get()+'\t'+entry4.get()+'\t'+entry5.get()+'\t'+entry6.get()+'\n')
			messagebox.showinfo('Title','Record updated')
		else:
			file.write(line)
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	file.close()

def nextrecord(event):
	file=open('sample.txt','r')
	global index
	index=index+1
	print(index)
	file.seek(index)
	try:
		c=file.readlines()
		xyz = c[index]
		l=list(xyz.split())
		entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
		entry1.insert(0,l[0]);entry2.insert(0,l[1]);entry3.insert(0,l[2]);entry4.insert(0,l[3]);entry5.insert(0,l[4]);entry6.insert(0,l[5]);
	except:
		messagebox.showinfo("Title", "@@@ NO MORE RECORDS @@@")
	file.close()


def prevrecord(event):
	file=open('sample.txt','r')
	global index
	index=index-1
	print(index)
	try:
		file.seek(index)
		c=file.readlines()
		xyz = c[index]
		l=list(xyz.split())
		entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
		entry1.insert(0,l[0]);entry2.insert(0,l[1]);entry3.insert(0,l[2]);entry4.insert(0,l[3]);entry5.insert(0,l[4]);entry6.insert(0,l[5]);
	except:
		messagebox.showinfo("Title", "@@@ NO MORE RECORDS @@@")
	file.close()


def firstrecord(event):
	file=open('sample.txt','r')
	global index
	index=0
	print(index)
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	file.seek(0)
	k=file.readline()
	k=k.split()
	entry1.insert(0,k[0]);entry2.insert(0,k[1]);entry3.insert(0,k[2]);entry4.insert(0,k[3]);entry5.insert(0,k[4]);entry6.insert(0,k[5]);
	file.close()

def lastrecord(event):
	file=open('sample.txt','r')
	count=0
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');
	for i in file:
		k=i
		count+=1
	k=k.split()
	entry1.insert(0,k[0]);entry2.insert(0,k[1]);entry3.insert(0,k[2]);entry4.insert(0,k[3]);entry5.insert(0,k[4]);entry6.insert(0,k[5]);
	global index
	
	index=count
	print(index)
	file.close()

def reset(event):
	entry1.delete(0,'end');entry2.delete(0,'end');entry3.delete(0,'end');entry4.delete(0,'end');entry5.delete(0,'end');entry6.delete(0,'end');

label0= Label(root,text="           STOCK MARKET DATABASE", font=("Helvetica", 30))
label0.grid(columnspan=6, padx=10, pady=10)

label1=Label(root,text='Company Name',font=("Helvetica", 12))
label1.grid(row=6,column=0, sticky=W, padx=10, pady=10)

label2=Label(root,text='Date',font=("Helvetica", 12))
label2.grid(row=7,column=0, sticky=W, padx=10, pady=10)

label3=Label(root,text='Open',font=("Helvetica", 12))
label3.grid(row=8,column=0, sticky=W, padx=10, pady=10)

label4=Label(root,text='High',font=("Helvetica", 12))
label4.grid(row=9,column=0, sticky=W, padx=10, pady=10)

label5=Label(root,text='Low',font=("Helvetica", 12))
label5.grid(row=10,column=0, sticky=W, padx=10, pady=10)

label6=Label(root,text='Close',font=("Helvetica", 12))
label6.grid(row=11,column=0, sticky=W, padx=10, pady=10)

entry1=Entry(root,font=("Helvetica", 12))
entry1.grid(row=6,column=1, padx=10, pady=10)

entry2=Entry(root,font=("Helvetica", 12))
entry2.grid(row=7,column=1, padx=10, pady=10)

entry3=Entry(root,font=("Helvetica", 12))
entry3.grid(row=8,column=1, padx=10, pady=10)

entry4=Entry(root,font=("Helvetica", 12))
entry4.grid(row=9,column=1, padx=10, pady=10)

entry5=Entry(root,font=("Helvetica", 12))
entry5.grid(row=10,column=1, padx=10, pady=10)

entry6=Entry(root,font=("Helvetica", 12))
entry6.grid(row=11,column=1, padx=10, pady=10)

button1=Button(root,text='Add new record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button1.bind('<Button-1>',addrecord)
button1.grid(row=12,column=0,padx=4, pady=10)

button2=Button(root,text='Remove record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button2.bind('<Button-1>',removerecord)
button2.grid(row=12,column=1,padx=4, pady=10)

button3=Button(root,text='Search record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button3.bind('<Button-1>',searchrecord)
button3.grid(row=12,column=2,padx=4, pady=10)

button4=Button(root,text='Update record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button4.bind('<Button-1>',updaterecord)
button4.grid(row=13,column=0,padx=4, pady=10)

button5=Button(root,text='Show next record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button5.bind('<Button-1>',nextrecord)
button5.grid(row=13,column=1,padx=4, pady=10)

button6=Button(root,text='Show previous record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button6.bind('<Button-1>',prevrecord)
button6.grid(row=14,column=2,padx=4, pady=10)


button7=Button(root,text='Show last record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button7.bind('<Button-1>',lastrecord)
button7.grid(row=13,column=2,padx=4, pady=10)

button8=Button(root,text='Show first record', bg="black", fg="white", width=20, font=("Helvetica", 12))
button8.bind('<Button-1>',firstrecord)
button8.grid(row=14,column=0,padx=4, pady=10)

button8=Button(root,text='Reset', bg="black", fg="white", width=20, font=("Helvetica", 12))
button8.bind('<Button-1>',reset)
button8.grid(row=14,column=1,padx=4, pady=10)


root.geometry('880x560')
root.resizable(width=False, height=False)
root.mainloop()