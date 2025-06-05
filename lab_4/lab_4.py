import sys

class Node:
    def __init__(self, key, value, color='RED'):
        self.key = key  # Ціна акції
        self.value = value  # Назва компанії
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, 'BLACK')
        self.root = self.NIL
    
    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        
        parent = None
        current = self.root
        
        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
                
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
            
        new_node.color = 'RED'
        self._fix_insert(new_node)
    
    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)
        
        self.root.color = 'BLACK'
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def find(self, key):
        return self._find_helper(self.root, key)
    
    def _find_helper(self, node, key):
        if node == self.NIL:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._find_helper(node.left, key)
        else:
            return self._find_helper(node.right, key)
    
    def print_tree(self):
        self._print_helper(self.root, "", True)
    
    def _print_helper(self, node, indent, last):
        if node != self.NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            
            print(f"{node.key} ({node.value}) [{node.color}]")
            self._print_helper(node.left, indent, False)
            self._print_helper(node.right, indent, True)
    
    def get_min(self):
        return self._get_min_helper(self.root)
    
    def _get_min_helper(self, node):
        while node.left != self.NIL:
            node = node.left
        return node if node != self.NIL else None
    
    def get_max(self):
        return self._get_max_helper(self.root)
    
    def _get_max_helper(self, node):
        while node.right != self.NIL:
            node = node.right
        return node if node != self.NIL else None

def main():
    stock_market = RedBlackTree()
    
    while True:
        print("\nІмітація ринку акцій")
        print("1. Додати акцію")
        print("2. Знайти акцію за ціною")
        print("3. Показати всі акції")
        print("4. Найдешевша акція")
        print("5. Найдорожча акція")
        print("6. Вийти")
        
        choice = input("Виберіть опцію: ")
        
        if choice == '1':
            company = input("Введіть назву компанії: ")
            try:
                price = float(input("Введіть ціну акції: "))
                stock_market.insert(price, company)
                print(f"Акція {company} з ціною {price} додана до ринку.")
            except ValueError:
                print("Невірний формат ціни! Спробуйте ще раз.")
        
        elif choice == '2':
            try:
                price = float(input("Введіть ціну для пошуку: "))
                node = stock_market.find(price)
                if node:
                    print(f"Знайдено: {node.value} з ціною {node.key}")
                else:
                    print("Акцію з такою ціною не знайдено.")
            except ValueError:
                print("Невірний формат ціни!")
        
        elif choice == '3':
            print("\nСписок всіх акцій (у форматі ціна - назва компанії):")
            stock_market.print_tree()
        
        elif choice == '4':
            min_node = stock_market.get_min()
            if min_node:
                print(f"Найдешевша акція: {min_node.value} з ціною {min_node.key}")
            else:
                print("Ринок акцій порожній.")
        
        elif choice == '5':
            max_node = stock_market.get_max()
            if max_node:
                print(f"Найдорожча акція: {max_node.value} з ціною {max_node.key}")
            else:
                print("Ринок акцій порожній.")
        
        elif choice == '6':
            print("Дякую за використання програми!")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()