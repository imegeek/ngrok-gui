import os
import psutil
import subprocess
from time import sleep
import requests
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ngrok GUI")
root.resizable(0, 0)

window_width = 600
window_height = 400

# Get the screen width and height.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center coordinates for positioning the window.
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))

# Set the geometry of the window to be centered on the screen.
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

def stop_ngrok():
	for proc in psutil.process_iter(['pid', 'name']):
		if "ngrok" in proc.info['name']:
			os.kill(proc.info['pid'], 9)
	text.set("No Link Generated")
	copy_button.config(state="disabled")
	btn.config(text="Start Tunnel", command=start_ngrok)

def close_window():
	stop_ngrok()
	root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)

def copy_link():
	"""
	Function to copy the forward link to the clipboard.
	"""
	forward_link = link.get()

	if forward_link:
		root.clipboard_clear()  # Clear the contents of the clipboard in tkinter.
		root.clipboard_append(forward_link)  # Append the forward link to the clipboard in tkinter.
		root.update()  # Update the tkinter window to set the copied forward link to the system clipboard.

def start_ngrok(config=False):
	stop_ngrok()
	host = host_output.get()
	port = port_output.get()
	protocol = combo_item.get().lower()
	process = subprocess.Popen(['ngrok', protocol, f"{host}:{port}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
	ngrok_pid.set(process.pid)
	process_output = []
	error_output = False
	text.set("Starting...")
	btn.config(text="Connecting...")
	root.update()
	
	# # Read and print the output line by line
	# for line in process.stdout:
	# 	print(line, end='')

	# # Wait for the process to finish
	# process.wait()

	sleep(2)

	if process.poll() == 0:
		for line in process.stdout:
			# process_output.append(line.strip())
			process_output.append(line)
		main_frame.pack_forget()
		log.pack(fill="both", expand=True)

	# print(process_output)

	for output in process_output:
		if "ERROR" in output:
			error_output = True
			log.insert(END, output)
			# Scroll to the bottom of the text widget
			log.see(END)
			# Update the GUI to display the new log line
			root.update()

	if not error_output:
		while True:
			try:
				response = requests.get("http://localhost:4040/api/tunnels")
				break
			except Exception:
				pass

		try:
			# print(response.json()["tunnels"][0]["public_url"])
			text.set(response.json()["tunnels"][0]["public_url"])
			link.set(text.get())
			copy_button.config(state="normal")
			btn.config(text="Stop Tunnel", command=stop_ngrok)
		except Exception:
			text.set("No Internet Connection!")
			btn.config(text="Start Tunnel")
	else:
		text.set("No Link Generated")

# start_ngrok("http", "8080")

ngrok_pid = IntVar()
ngrok_pid.set(-1)
text = StringVar()
text.set("No Link Generated")
host_output = StringVar()
port_output = StringVar()
combo_item = StringVar()
combo_item.set("HTTP")
link = StringVar()

# def padding(*args):
# 	host = host_output.get()
# 	if not host:
# 		host_input.insert(0, " ")

# def placeholder(widget, *args):
# 	print(widget.get())

def validate_port(*args):
	port = port_output.get()

	def restore_port(port):
		port_input.config(state="normal")
		port_input.config(fg="black")
		port_input.delete(0, END)
		port_input.insert(0, port)

	if not port.isdigit():
		number = [number for number in port if number.isdigit()]
		port_input.delete(0, END)
		port_input.insert(0, ''.join(number))
	else:
		if int(port) > 65535:
			# root.focus_force()
			port_input.config(fg="red")
			port_input.delete(0, END)
			port_input.insert(0, "Port must be 0-65535")
			port_input.config(state="readonly")
			root.after(1200, restore_port, port[0:-1])

# host_output.trace_add(mode="write", callback=lambda *e: placeholder(host_input, e))
# port_output.trace_add(mode="write", callback=lambda *e: placeholder(port_input, e))
port_output.trace_add(mode="write", callback=validate_port)

Label(text="Ngrok GUI", font=("Verdana", 24), fg="#3d3d3d").pack(pady=10)

main_frame = Frame(root, width=550, height=300, relief="ridge", borderwidth=4)
main_frame.pack()

log = Text(root, wrap='word', width=100, height=10, fg="red", font=("Roboto", 11), padx=10)

link_frame = Frame(main_frame, width=390, height=40, relief="ridge", borderwidth=2, bg="#e4e4e4")
link_frame.place(relx=0.05, rely=0.1)

copy_button = Button(main_frame, cursor="hand2", width=6, text="Copy", borderwidth=2, relief="ridge", command=copy_link, bg="#77C2FF", activebackground="#77C2FF", font=("Verdana", 11), padx=10, pady=5, state="disabled")
copy_button.place(relx=0.81, rely=0.1)

lbl = Label(link_frame, textvariable=text, font=("Verdana", 11), bg="#e4e4e4")
lbl.place_configure(relx=0.02, rely=0.5, anchor="w")

host_input_frame = Frame(main_frame, width=200, height=25, bg="white", highlightbackground="#808080", highlightthickness=1)
host_input_frame.place(relx=0.5, rely=0.4, anchor=CENTER)

host_input = Entry(host_input_frame, textvariable=host_output, insertwidth=1, width=21, fg="#000", font=("Roboto", 12), borderwidth=0)
host_input.place(relx=0.02, rely=0.5, anchor="w")
host_input.insert(0, "localhost")

port_input = Entry(main_frame, textvariable=port_output, insertwidth=1, width=20, fg="#000", font=("Roboto", 12), borderwidth=0, highlightbackground="#808080", highlightthickness=1)
port_input.place(relx=0.06, rely=0.6)
port_input.insert(0, "8080")

protocol_box = ttk.Combobox(main_frame, textvariable=combo_item, font=("Roboto", 12))
protocol_box.place(relx=0.585, rely=0.6)

protocol_box['values'] = [
	"HTTP",
	"TCP"
]

protocol_box.current()

btn = Button(main_frame, text="Create Tunnel", command=start_ngrok, cursor="hand2", width=25, borderwidth=2, relief="ridge", bg="#77C2FF", activebackground="#77C2FF", font=("Verdana", 12), pady=5)
btn.place(relx=0.5, rely=0.85, anchor=CENTER)

# btn["command"] = start_ngrok

main_frame.bind("<Button-1>", lambda e : root.focus_force())
root.mainloop()
