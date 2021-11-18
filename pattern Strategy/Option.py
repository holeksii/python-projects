from task04.LinkedList import LinkedList
from Strategy import Strategy
from task04.Validation import validation as VLD
from task04.task_funсtions import deleteElements

class Option:
    
    def __init__(self, instance):
        self.linked_list = instance


    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, instance):
        if not isinstance(instance, LinkedList):
            raise TypeError()
        self._instance = instance


    def option1(self):
        ok = False
        while not ok:
            print("low bound: ", end=' ')
            low = VLD.get_number()

            print("up bound: ", end=' ')
            up = VLD.get_number()

            print("size of list: ", end=' ')
            size = VLD.get_strictly_positive()
            
            
            if len(self.linked_list) != 0:
                print("position to paste: ", end=' ')
                k = VLD.get_index(len(self.linked_list) + 1)
                if k != len(self.linked_list):
                    try:
                        for item in Strategy.strategy1(low, up, size):
                            self.linked_list.insert(k, item)
                            k += 1
                        ok = True
                    except Exception as e:
                        print(e)
                else:
                    for item in Strategy.strategy1(low, up, size):
                        self.linked_list.append(item)
                    ok = True
            else:
                try:
                    self.linked_list = Strategy.strategy1(low, up, size)
                    ok = True
                except Exception as e:
                    print(e)
                    
                    
        

    def option2(self):
        ok = False
        while not ok:
            print("FILEPATH: ", end=' ')
            FILEPATH = input()
            
            if len(self.linked_list) != 0:
                print("position to paste: ", end=' ')
                k = VLD.get_index(len(self.linked_list) + 1)
                if k != len(self.linked_list):
                    try:
                        for item in Strategy.strategy2(FILEPATH):
                            self.linked_list.insert(k, item)
                            k += 1
                        ok = True
                    except Exception as e:
                        print(e)
                else:
                    for item in Strategy.strategy2(FILEPATH):
                        self.linked_list.append(item)
                    ok = True
            else:
                try:
                    self.linked_list = Strategy.strategy2(FILEPATH)
                    ok = True
                except Exception as e:
                    print(e)
                


    def option3(self):
        while True:
            print("choose strategy:\n1 -- generate\n2 -- from file")
            try:
                op = int(input())
            except:
                print("invalid option")
                continue
            if op == 1:
                self.option1()
                break
            elif op == 2:
                self.option2()
                break
            else:
                print("invalid option")
                continue
            

    def option4(self):
        print("position: ", end=' ')
        k = VLD.get_index(len(self.linked_list))
        self.linked_list.pop(k)

    def option5(self):
        while True:
            print("low bound: ", end=' ')
            low = VLD.get_index(len(self.linked_list))
            
            print("up bound: ", end=' ')
            up = VLD.get_index(len(self.linked_list))
            
            if not VLD.a_bigger_b(up, low):
                print("invalid bounds")
                continue
            for i in range(up - low + 1):
                self.linked_list.pop(low)
            break


    def option6(self):
        deleteElements(self.linked_list)
        

    def print_linked_list(self):
        print()
        if len(self.linked_list) == 0:
            print("List is empty")
            return
        for item in self.linked_list:
            print(item, end=' ')
        print(end='\n\n')


    def save(self):
        while True:
            print(f"save to {self.linked_list.FILEPATH}\n(y/n)?")
            answr = input()
            if answr == 'y':
                self.linked_list.dump_to_json()
                break
            elif answr == 'n':
                break
            else:
                continue
