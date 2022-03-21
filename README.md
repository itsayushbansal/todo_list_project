# **TODO LIST**

Repository of a TODO List Application

### **Dependencies**
```
Python >= 3.8
Sqlite
Docker
```

### **Repository Setup**
>Clone Repository
```
$ git clone https://github.com/itsayushbansal/todo_list_project.git
```
>Navigate to the Repository
```
$ cd todo_list_project
```

### **Build Application**
>Build Docker Image

(An Admin user will be created by default with both username and password as 'admin')
```
$ docker build . -t django-todo-list-v0.0
```

### **Run Application**
>Run Docker Image 
```
$ docker run -it -p 8000:8000 django-todo-list-v0.0
```
