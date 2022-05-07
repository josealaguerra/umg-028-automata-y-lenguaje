import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
import Drawpy
n = 0

side1 = "left"
side2 = "right"

start = {"farmer":side1, "wolf":side1, "goat":side1, "cabbage":side1}
meta = {"farmer":side2, "wolf":side2, "goat":side2, "cabbage":side2}

_Queue =[]
notrepet =[]
_patch  = []

notrepet.append(start)
_Queue.append(start)


def validate_state(state):
    if state["wolf"] == state["goat"] and state["wolf"] != state["farmer"]:
        return False
    elif state["goat"] == state["cabbage"] and state["cabbage"] != state["farmer"]:
        return False
    else:
        return True

def Generar_states(state_actual, _patch ,dot):
    global n
    list_state = []
    new_state = dict(state_actual)
    _nodes = [w[0] for w in _patch.copy()] # se supone que obtengo todas las llaves de los dict
    if state_actual not in _nodes: #si aun no se ah creado el nodo para ese estado
        n, _patch, dot = Drawpy.Make_Node(state_actual, new_state, n, _patch, dot, 0)
    if state_actual["farmer"] == side2:  
        new_state["farmer"] = side1  
        if validate_state(new_state) and new_state not in notrepet:
            list_state.append(dict(new_state)) 
            notrepet.append(dict(new_state))
            n, _patch, dot = Drawpy.Make_Node(state_actual, new_state, n, _patch, dot, 1)

        for k, v in new_state.items():
            if k != "farmer":
                if v == side2: 
                    new_state[k] = side1  
                    if validate_state(new_state) and new_state not in notrepet:
                        list_state.append(dict(new_state))
                        notrepet.append(dict(new_state))
                        n, _patch, dot = Drawpy.Make_Node(state_actual, new_state, n, _patch, dot, 1)
                    new_state[k] = side2 
    else: 
        new_state["farmer"] = side2
        for k, v in new_state.items():
            if k != "farmer":
                if v == side1:
                    new_state[k] = side2
                    if validate_state(new_state) and new_state not in notrepet:
                        list_state.append(dict(new_state))
                        notrepet.append(dict(new_state))
                        n, _patch, dot = Drawpy.Make_Node(state_actual, new_state, n, _patch, dot, 1)
                    new_state[k] = side1
    return list_state

#Tipo: (0) en profundidad (1) anchura, (2)profundidad limitada
def algoritmo(tipo, _patch, dot):
    while _Queue:
        if tipo == 0:
            node = _Queue.pop() #en profundidad
        elif tipo == 1:
            node = _Queue.pop(0) # anchura

        if node != meta: 
            temp_list = Generar_states(node, _patch, dot)[:]
            print("Generate", temp_list)
            _Queue.extend(temp_list.copy())      
        elif node == meta:
            print("End......")
            break 



dot = graphviz.Digraph(comment='Arbol de decisión')
algoritmo(0, _patch, dot) #LLAMAMO EL METEDO PRINCIPAL. 
dot.render()