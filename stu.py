from tkinter import*
from tkinter.messagebox import *
from tkinter.scrolledtext import*
from sqlite3 import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def f1():
	root.withdraw()
	add_st.deiconify()

		
def f2():
	add_st.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	view_st.deiconify()


def f4():
	view_st.withdraw()
	root.deiconify()

def f5():
	root.withdraw()
	update_st.deiconify()


def f6():
	update_st.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	delete_st.deiconify()

def f8():
	delete_st.withdraw()
	root.deiconify()
def f9():
	figure = plt.figure
	plt.show()
	

def addinput():
	con = None
	try:
		con = connect("students.db")
		sql = "create table if not exists student (rno int primary key, name text, marks int) "
		cursor = con.cursor()
		cursor.execute(sql)
		rno = 0
		name = ''
		marks = 0
		sql = "insert into student values('%d','%s','%d')"
		rno = add_st_entrno.get()
		name = add_st_entname.get()
		marks = add_st_entmarks.get()
		if (rno and name and marks):
			cursor.execute(sql % (int(rno), name, int(marks)))
			showinfo("Inserted")
		elif((rno and name and marks)==''):
			showinfo("Insert all records please")
		elif(rno<0):
			showinfo("Please insert positive integers")
		elif(marks<0 or marks>100):
			showinfo("Marks should be in range of 0 to 100")
		elif not(("A" <= name and name <= "Z") or ("a" <= name and name <= "z")):
			showinfo("name should contain alphabets")
		elif (name.len< 2):
			raise ValueError("name must be at least 2 character long")
		else:
			showinfo("good to go")
		con.commit()
	except Exception as e:
		print("issues", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def deleteinput():
	con = None
	try:
		con = connect("students.db")
		sql = "delete from student where rno = '%d'"
		cursor = con.cursor()
		rno = int(delete_st_entrno.get())
		cursor.execute(sql % rno)
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Record deleted")
		else:
			showinfo("Record does not exists")
		con.commit()
	except Exception as e:
		print("issues", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()


def updateinput():
	con = None
	cursor = None
	try:
		con = connect("students.db")
		cursor = con.cursor()
		rno = int(update_st_entrno.get())
		if rno <= 0:
			showerror("Invalid ROLL NO.")
		marks = int(update_st_entmarks.get())
		if marks<0 or marks>50:
				showerror("Invalid MARKS")
		sql = "update student set marks='%d' where rno='%d'"
		args = (marks, rno)
		cursor.execute(sql%args)
		showinfo("Success", str(cursor.rowcount) + " record updated")
		sql = "select marks from student"
		cursor.execute(sql)
		sel = cursor.fetchall()
		con.commit()
	except Exception as e:
		print("issues", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

	
def viewstudent():
	con = None
	try:
		con = connect("students.db")
		sql = "select * from student"
		cursor = con.cursor()
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			print("rno", d[0], "name", d[1], "marks", d[2])
	except Exception as e:
		print("issues", e)
	finally:
		if con is not None:
			con.close()





root =Tk()
root.title("S.M.S")
root.geometry("400x400+400+200")
root.configure(background='powderblue')


b1 = Button(root,text = "ADD",pady=10,padx=45, width = 10,command=f1)  
b1.pack()  
b1.place(x=120,y=30)

b2 = Button(root,text = "UPDATE",pady=10,padx=45,width = 10,command = f5)  
b2.pack()  
b2.place(x=120,y=90)

b3 = Button(root,text = "VIEW",pady=10,padx=45,width = 10,command=viewstudent)
b3.pack()  
b3.place(x=120,y=150)

b4 = Button(root,text = "DELETE", pady=10,padx=45,width = 10,command = f7)  
b4.pack()  
b4.place(x=120,y=210)

b5 = Button(root,text = "CHARTS", pady=10,padx=45,width = 10,command = f9)
b5.pack()
b5.place(x=120,y=270)

#T = Text(root, height = 3, width = 45,bg="powderblue",bd=4)
#T.pack()
#T.place(x=20,y=320)


add_st = Toplevel(root)
add_st.title("Add Student")
add_st.geometry("500x500+400+200")
add_st.configure(background='mint cream')

add_st_lblrno = Label(add_st, text="Enter roll no", font=('arial', 18, 'bold')) 
add_st_entrno = Entry(add_st, bd=5, font=('arial', 18, 'bold'))
add_st_lblname = Label(add_st, text="Enter name", font=('arial', 18, 'bold'))
add_st_entname = Entry(add_st, bd=5, font=('arial', 18, 'bold'))
add_st_btnsave = Button(add_st, text="Save", font=('arial', 18, 'bold'),command= addinput)
add_st_btnback = Button(add_st, text="Back", font=('arial', 18, 'bold'), command=f2)
add_st_lblmarks = Label(add_st, text="Enter Marks", font=('arial', 18, 'bold'))
add_st_entmarks = Entry(add_st, bd=5, font=('arial', 18, 'bold'))


add_st_lblrno.pack(pady=10)
add_st_entrno.pack(pady=10)
add_st_lblname.pack(pady=10)
add_st_entname.pack(pady=10)
add_st_lblmarks.pack(pady=10)
add_st_entmarks.pack(pady=10)
add_st_btnsave.pack(pady=10)
add_st_btnback.pack(pady=10)
add_st.withdraw()


view_st = Toplevel(root)
view_st.title("View Student")
view_st.geometry("400x400+400+200")
view_st.configure(background='lavender')

view_st_data = ScrolledText(view_st, width=28, height = 10, font =('arial', 18, 'bold'))
view_st_btnback = Button(view_st,text='Back',font=('arial',18,'bold'),command=f2)


view_st_data.pack(pady=10)
view_st_btnback.pack(pady=10)
view_st.withdraw()


update_st = Toplevel(root)
update_st.title("Update Student")
update_st.geometry("500x500+400+200")

update_st_lblrno = Label(update_st, text="Enter Roll No to Update", font=('arial', 18, 'bold'))
update_st_entrno = Entry(update_st, bd=5, font=('arial', 18, 'bold'))
update_st_lblname = Label(update_st, text="Enter New name", font=('arial', 18, 'bold'))
update_st_entname = Entry(update_st, bd=5, font=('arial', 18, 'bold'))
update_st_btnsave = Button(update_st, text="Update", font=('arial', 18, 'bold'),command= updateinput)
update_st_btnback = Button(update_st, text="Back", font=('arial', 18, 'bold'), command=f2)
update_st_lblmarks = Label(update_st, text="Enter new Marks", font=('arial', 18, 'bold'))
update_st_entmarks = Entry(update_st, bd=5, font=('arial', 18, 'bold'))



update_st_lblrno.pack(pady=10)
update_st_entrno.pack(pady=10)
update_st_lblname.pack(pady=10)
update_st_entname.pack(pady=10)
update_st_lblmarks.pack(pady=10)
update_st_entmarks.pack(pady=10)
update_st_btnsave.pack(pady=10)
update_st_btnback.pack(pady=10)
update_st.withdraw()


delete_st = Toplevel(root)
delete_st.title("Delete Student")
delete_st.geometry("500x500+400+200")

delete_st_lblrno = Label(delete_st, text="enter rno", font=('arial', 18, 'bold')) 
delete_st_entrno = Entry(delete_st, bd=5, font=('arial', 18, 'bold'))
delete_st_btndelete = Button(delete_st, text="delete", font=('arial', 18, 'bold'),command=deleteinput)
delete_st_btnback = Button(delete_st, text="Back", font=('arial', 18, 'bold'), command=f8)



delete_st_lblrno.pack(pady=10)
delete_st_entrno.pack(pady=10)
delete_st_btndelete.pack(pady=10)
delete_st_btnback.pack(pady=10)
delete_st.withdraw()


root.mainloop()
