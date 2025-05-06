import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog  # 사용자로부터 입력값을 받기 위한 대화 상자 제공
from todo_func import Todo_list
import pymysql

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("640x480+100+100")

        self.todo_list = Todo_list()
        
        title = tk.Label(root, text="Todo List 항목을 작성해주세요", width=25, height=5, fg="black", relief="ridge", bg="ivory")
        title.pack()

        self.listbox = tk.Listbox(root, selectmode='extended', height=0)
        self.listbox.pack(pady=10)

        # 할 일 추가 버튼
        add_button = tk.Button(root, text="할 일 추가", width=15, command=self.add_todo_popup)
        add_button.pack(pady=10)

        # 할 일 삭제 버튼
        delete_button = tk.Button(root, text="선택 항목 삭제", width=15, command=self.delete_selected_todo)
        delete_button.pack(pady=10)

        # 완료 버튼
        finish_button = tk.Button(root, text="저장", width=15, command=self.finish)
        finish_button.pack(pady=10)

        quit_button = tk.Button(root, text="종료", width=15, command=self.retryButton)
        quit_button.pack(pady=10)
        
        # 할 일 목록 초기화
        self.refresh_listbox()

    def add_todo_popup(self):
        """
        팝업창을 통해 할 일을 입력받아 목록에 추가합니다.
        """
        task = tk.simpledialog.askstring("할 일 추가", "추가할 할 일을 입력하세요:")  # "창 이름", "페이지 안의 글씨"
        if task:  # 입력값이 있을 때만 추가
            self.listbox.insert(tk.END, task)
            self.todo_list.todo_list.append(task)  # 메모리 목록에 추가

    def delete_selected_todo(self):
        """
        선택한 항목을 삭제하는 함수
        """
        selected_tasks = self.listbox.curselection()  # curselection()은 현재 선택된 항목의 인덱스들을 반환합니다.
        if not selected_tasks:
            tk.messagebox.showwarning("삭제 오류", "삭제할 항목을 선택하세요.")
            return

        for index in selected_tasks[::-1]:  # 역순으로 삭제
            task = self.listbox.get(index)
            self.listbox.delete(index)
            self.todo_list.todo_list.remove(task)  # 메모리 목록에서도 삭제

        tk.messagebox.showinfo("삭제 완료", "선택한 할 일이 삭제되었습니다.")

    def finish(self):
        """
        현재 GUI에 입력된 할 일 목록을 가져와 파일에 저장하는 메서드입니다.
        사용자가 할 일을 모두 입력하고 '저장' 버튼을 눌렀을 때 실행됩니다.
        """
        
        # listbox 위젯에서 현재 저장된 모든 항목(할 일)을 가져옵니다.
        # get(0, tk.END)는 0번 인덱스(처음)부터 마지막(tk.END)까지의 모든 아이템을 튜플 형태로 반환합니다.
        tasks = self.listbox.get(0, tk.END)

        # 가져온 할 일 목록을 TodoList 클래스의 add_todo 메서드를 이용해 저장합니다.
        # self.todo_list는 할 일 데이터를 관리하는 별도의 객체입니다.
        # add_todo는 보통 이 데이터를 파일로 저장하거나 내부 목록에 추가하는 기능을 담당합니다. (todo_func.py에 add_todo 구현 완료)
        self.todo_list.add_todo(tasks)

        # 사용자에게 저장이 완료되었음을 알리는 메시지 박스를 띄웁니다.
        # 첫 번째 인자는 제목("저장 완료"), 두 번째 인자는 메시지 내용입니다. 
        tk.messagebox.showinfo("저장 완료", "할 일 목록이 파일에 저장되었습니다.")


    def refresh_listbox(self):
        """
        파일에서 할 일 목록을 불러와 Listbox에 표시합니다.
        """
        self.todo_list.import_todo()  # 파일에서 할 일 목록을 불러옴
        self.listbox.delete(0, tk.END)  # 기존 항목 초기화
        for task in self.todo_list.todo_list:
            self.listbox.insert(tk.END, task)
            
    def quit(self):
        self.root.quit()
        
    def retryButton(self):
        reButton = tk.messagebox.askokcancel("종료", "종료하시겠습니까?")
        if reButton == True:
            self.root.quit()
        else:
            tk.messagebox.showinfo("종료 취소", "취소되었습니다.")

# tkinter 윈도우 생성 및 실행
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
