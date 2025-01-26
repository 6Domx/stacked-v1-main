from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import heapq
from queue import Queue
import logging
import sys
sys.path.append('/path/to/directory')
from LinkedList import LinkedList

app = Flask(__name__)

@app.route("/")
def hero():
    return render_template("hero.html")

@app.route("/profile")
def pofile():
    members = [
        {
            "name": "ANGELICA MARI S. VICTORINO",
            "course_section": "BSCPE 2-2",
            "quote": "I don’t chase, I attract",
            "image": "assets/member-1.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "HANNAH NYTRISHA D. CASABUENA",
            "course_section": "BSCPE 2-2",
            "quote": "Dream boldly, act fearlessly, and live with purpose.",
            "image": "assets/member-2.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "JANNINA ALEXA I. TABOR",
            "course_section": "BSCPE 2-2",
            "quote": "Let go and be unhurried",
            "image": "assets/member-3.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "CASEY E. DE VERA",
            "course_section": "BSCPE 2-2",
            "quote": "When the pain penetrates, code resonates.",
            "image": "assets/member-4.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "MIGUEL DOMINIC DG. PAYUMO",
            "course_section": "BSCPE 2-2",
            "quote": "Carpe diem, seize the day.",
            "image": "assets/member-5.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "JOSEPH S. ELULA",
            "course_section": "BSCPE 2-2",
            "quote": "When life gives you lemons, make lemonade.",
            "image": "assets/member-6.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "JOHN LUIS GEPILA",
            "course_section": "BSCPE 2-3",
            "quote": "Success is earned through effort, not given by chance.",
            "image": "assets/member-7.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link4"},
                {"image": "assets/victorino-project-1.png", "link": "link5"},
                {"image": "assets/victorino-project-1.png", "link": "link6"},
            ]
        },
    ]
    return render_template('profile.html', members=members)

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/stacks')
def stacks():
    return render_template('stacks.html')  # Serve the HTML file

# Graph structure for MRT lines
class MRTGraph:
    def __init__(self):
        self.graph = {}
    
    def add_station(self, station):
        if station not in self.graph:
            self.graph[station] = {}
    
    def add_connection(self, station1, station2, distance):
        self.add_station(station1)
        self.add_station(station2)
        self.graph[station1][station2] = distance
        self.graph[station2][station1] = distance
    
    def shortest_path(self, start, end):
        queue = [(0, start)]
        distances = {station: float('inf') for station in self.graph}
        distances[start] = 0
        previous_nodes = {station: None for station in self.graph}
        
        while queue:
            current_distance, current_station = heapq.heappop(queue)
            
            if current_station == end:
                path = []
                while current_station is not None:
                    path.insert(0, current_station)
                    current_station = previous_nodes[current_station]
                return path, distances[end]
            
            for neighbor, weight in self.graph[current_station].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_station
                    heapq.heappush(queue, (distance, neighbor))
        
        return None, float('inf')

mrt = MRTGraph()

# Example MRT stations and distances
connections = [
    ("Taft Avenue", "Magallanes", 2),
    ("Magallanes", "Ayala", 2),
    ("Ayala", "Buendia", 2),
    ("Buendia", "Guadalupe", 2),
    ("Guadalupe", "Boni", 2),
    ("Boni", "Shaw Boulevard", 2),
    ("Shaw Boulevard", "Ortigas", 2),
    ("Ortigas", "Santolan Anapolis", 2),
    ("Santolan Anapolis", "Araneta Center Cubao", 2),
    ("Araneta Center Cubao", "GMA Kamuning", 2),
    ("GMA Kamuning", "Quezon Avenue", 2),
    ("Quezon Avenue", "North Avenue", 2),
]

for connection in connections:
    mrt.add_connection(*connection)

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    path = None
    distance = None
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        path, distance = mrt.shortest_path(start, end)
    
    return render_template('graph.html', stations=mrt.graph.keys(), path=path, distance=distance)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = Node(value)
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = Node(value)
                return
            else:
                queue.append(current.right)

    def traverse(self, order_type):
        result = []
        
        def preorder(node):
            if node:
                result.append(str(node.value))
                preorder(node.left)
                preorder(node.right)
        
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(str(node.value))
                inorder(node.right)
        
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(str(node.value))
        
        if order_type == 'preorder':
            preorder(self.root)
        elif order_type == 'inorder':
            inorder(self.root)
        elif order_type == 'postorder':
            postorder(self.root)
            
        return result

    def search(self, target):
        if not self.root:
            return False
            
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if str(current.value) == str(target):
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def get_tree_structure(self, node, level=0):
        if not node:
            return []
        result = [{"value": node.value, "level": level}]
        if node.left:
            result.extend(self.get_tree_structure(node.left, level + 1))
        if node.right:
            result.extend(self.get_tree_structure(node.right, level + 1))
        return result

binary_tree = BinaryTree()

@app.route('/binary')
def binary():
    return render_template('binary.html')

@app.route('/insert', methods=['POST'])
def insert_value():
    data = request.get_json()
    try:
        value = data['value'].strip()
        if not value:
            return jsonify({"success": False, "error": "Please enter a value"})
        
        binary_tree.insert(value)
        tree_structure = binary_tree.get_tree_structure(binary_tree.root)
        
        return jsonify({
            "success": True, 
            "tree": tree_structure,
            "traversals": {
                "preorder": binary_tree.traverse('preorder'),
                "inorder": binary_tree.traverse('inorder'),
                "postorder": binary_tree.traverse('postorder')
            }
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/search', methods=['POST'])
def search_value():
    data = request.get_json()
    try:
        value = data['value'].strip()
        if not value:
            return jsonify({"success": False, "error": "Please enter a value to search"})
        
        found = binary_tree.search(value)
        return jsonify({
            "success": True,
            "found": found,
            "message": "Match found!" if found else "No match found."
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/clear', methods=['POST'])
def clear_tree():
    try:
        global binary_tree
        binary_tree = BinaryTree()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
    
    class Node:
        def __init__(self, data):
            self.data = data  
        self.next = None  

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            return
        current = self.front
        while current:
            print(current.data, end=" -> " if current.next else " -> None\n")
            current = current.next

if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()

    print(f"Dequeued: {q.dequeue()}")
    print(f"Front item: {q.peek()}")
    print(f"Queue size: {q.get_size()}")

    q.display()

q = Queue()

@app.route('/queue')
def queue():
    return render_template('queue.html', queue=q.display(), size=q.get_size())

@app.route('/enqueue', methods=['POST'])
def enqueue():
    if request.method == 'POST':
        data = request.form['data']
        try:
            value = int(data)
            q.enqueue(value)
            return redirect(url_for('queue'))
        except ValueError:
            return render_template('queue.html', queue=q.display(), size=q.get_size(), error="Please enter a valid integer.")

@app.route('/dequeue', methods=['POST'])
def dequeue():
    q.dequeue()
    return redirect(url_for('queue'))

@app.route('/peek', methods=['POST'])
def peek():
    front_item = q.peek()
    return render_template('queue.html', queue=q.display(), size=q.get_size(), front_item=front_item)

@app.route('/clear', methods=['POST'])
def clear():
    q.clear()
    return redirect(url_for('queue'))

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

@app.route('/sort')
def sort():
    return render_template('sort.html')

linked_list =  LinkedList()

logging.basicConfig(level=logging.DEBUG)

@app.route('/linked_list')
def linked():
    return render_template('linked.html', linked_list=linked_list.print_list())

@app.route('/update', methods=['POST'])
def update():
    print("POST request received at /update")  # Add this for debugging
   
    operation = request.form.get('operation')
    data = request.form.get('data')
    
    logging.debug(f"Received operation: {operation}")
    logging.debug(f"Received data: {data}")
    
    if not operation:
        flash ('No operation provided', 'error')
        return render_template('linked.html', linked_list=linked_list.print_list())
    
    # Validate the data when required
    if operation in ["insert_beginning", "insert_end", "remove_at"] and not data:
        flash ('Please provide data for the operation', 'error')
        return render_template('linked.html', linked_list=linked_list.print_list())

    try:
        # Operations based on the button clicked
        if operation == "insert_beginning" and data:
            linked_list.insert_at_beginning(data)
            flash(f'Inserted {data} at the beginning.', 'success')
        elif operation == "insert_end" and data:
            linked_list.insert_at_end(data)
            flash(f'Inserted {data} at the end.', 'success')
        elif operation == "remove_beginning":
            if linked_list.head:  # If the list isn't empty
                removed_data = linked_list.remove_beginning()
                flash(f"Removed '{removed_data}' from the beginning.", 'success')
            else:
                flash("The list is empty. No element to remove.", 'error')
        elif operation == "remove_end":
            if linked_list.head:  # If the list isn't empty
                removed_data = linked_list.remove_end()
                flash(f"Removed '{removed_data}' from the end.", 'success')
            else:
                flash("The list is empty. No element to remove.", 'error')
        elif operation == "remove_at" and data:
            found = linked_list.search(data)
            if found:
                linked_list.remove_at(data)
                flash(f"Removed '{data}' from the list.", 'success')
            else:
                flash(f"Data '{data}' not found in the list.", 'error')
        elif operation == "search":
            found = linked_list.search(data)
            flash(f"Data '{data}' found in the list." if found else f"Data '{data}' not found in the list.", 'info')
        else:
            flash('Invalid operation.', 'error')
        
    except Exception as e:
        logging.error(f"Error occurred: {e}")  # Log error for debugging
        flash(f"An error occurred: {str(e)}", 'error')
        
    return render_template('linked.html', linked_list=linked_list.print_list())

class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,data):
        new_node = Node (data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head: 
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
    def remove_beginning(self):
        if self.head:
            removed_data = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return removed_data
        else:
            return None

    def remove_end(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            removed_data = self.head.data
            self.head = self.tail = None
            return removed_data
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            removed_data = self.tail.data
            current.next = None
            self.tail = current
            return removed_data
    
    def remove_at(self,data):
        if self.head:
            if self.head.data == data:
                self.remove_beginning()
                return
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    if current.next is None:  
                        self.tail = current
                    return
                current = current.next
                
    def search(self, data):
        current = self.head  
        while current:
            if current.data == data:
                print(f"Data {data} found in the list.")
                return True
            current = current.next
        print(f"Data {data} not found in the list.")
        return False

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def to_list(self):
        """Return the linked list as a regular Python list."""
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result
            
Linked_list = LinkedList()

if __name__ == "__main__":
    app.run(debug=True)


