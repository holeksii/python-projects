from List.LinkedList import LinkedList
from patterns.Strategy.Strategy import Strategy
from List.Validation import validation as VLD
from List.task_funсtions import deleteElements
from patterns.Observer.Observer import Observer, Event

class Option:
    
    def __init__(self, instance):
        self.linked_list = instance
        self.changes = []
        self.observe = Observer()


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
            
            i = 0
            if len(self.linked_list) != 0:
                print("position to paste: ", end=' ')
                k = VLD.get_index(len(self.linked_list) + 1)
                i = k
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
        
        
        self.changes.append((Event("add", old_list="[]", position=str(i), new_list=str(self.linked_list)).to_dict()))
        self.observe.update(self.changes)
        
                    
        

    def option2(self):
        ok = False
        while not ok:
            print("FILEPATH: ", end=' ')
            FILEPATH = input()
            i = 0
            if len(self.linked_list) != 0:
                print("position to paste: ", end=' ')
                k = VLD.get_index(len(self.linked_list) + 1)
                i = k
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
        
        self.changes.append((Event("add", old_list="[]", position=str(i), new_list=str(self.linked_list)).to_dict()))
        self.observe.update(self.changes)


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
        
        old = str(self.linked_list)
        self.linked_list.pop(k)
        
        self.changes.append((Event("delete", old_list=old, position=str(k), new_list=str(self.linked_list)).to_dict()))
        self.observe.update(self.changes)



    def option5(self):
        while True:
            print("low bound: ", end=' ')
            low = VLD.get_index(len(self.linked_list))
            
            print("up bound: ", end=' ')
            up = VLD.get_index(len(self.linked_list))
        
            
            if not VLD.a_bigger_b(up, low):
                print("invalid bounds")
                continue
            
            old = str(self.linked_list)
            
            for i in range(up - low + 1):
                self.linked_list.pop(low)
                
                
            self.changes.append(Event("delete", old_list=old, range=f"[{low}, {up}]", new_list=str(self.linked_list)).to_dict())
            self.observe.update(self.changes)
                
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
