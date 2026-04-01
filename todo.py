import json
import os

DATA_FILE="todos,json"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,'r',encoding='uft-8')as f:
            data=json.load(f)
            return data.get("todos",[])
    return[]

def save_todos(todos):
    with open(DATA_FILE,'w',encoding='utf-8')as f:
        json.dump({"todos":todos},f,ensure_ascii=False,indent=4)

def list_todos(todos):
    if not todos:
        print("暂无待办事项。")
        return
    print("ID | 状态 | 内容")
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["completed"] else "✗"
        print(f"{i:2} | {status} | {todo['task']}")

def add_todos(todos,task):
    todos.append({"task":task,"completed":False})
    print(f"已添加：{task}")

def mark_done(todos,index):
    if 1<=index<=len(todos):
        todos[index-1]["completed"]=True
        print(f"已标记完成:{todos[index-1]['task']}")
    else:
        print("无效序号。")

def delete_todo(todos,index):
    if 1<=index<=len(todos):
        removed=todo.pop(index-1)
        print(f"已删除：{removed['task']}")
    else:
        print("无效序号。")


def main():
    todos=load_todos()
    print("欢迎使用待办事项工具！输入help查看命令。")
    while True:
        cmd=input("\n>").strip()
        if not cmd:
            continue

        parts=cmd.split(maxsplit=1)
        command=parts[0].lower()

        if command=="add" and len(parts)>1:
            add_todos(todos,parts[1])
        elif command=="list":
            list_todos(todos)
        elif command=="done" and len(parts)>1:
            try:
                index=int(parts[1])
                mark_done(todos,index)
            except ValueError:
                print("请输入数字序号。")
        elif command=="delete" and len(parts)>1:
            try:
                index=int(parts[1])
                delete_todo(todos,index)
            except ValueError:
                print("请输入数字序号。")
        elif command in("quit","exit"):
            save_todos(todos)
            print("已保存，再见！")
            break
        elif command=="help":
            print("可用命令：")
            print("  add <任务内容>   - 添加任务")
            print("  list            - 列出所有任务")
            print("  done <序号>     - 标记任务为完成")
            print("  delete <序号>   - 删除任务")
            print("  quit / exit     - 退出程序")
        else:
            print("无效命令，输入help查看帮助。")

if __name__ == "__main__":
    main()


























 
