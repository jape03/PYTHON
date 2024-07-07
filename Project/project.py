from collections import deque

class CFG:
    def __init__(self, non_terminals, terminals, productions, start_symbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def generate(self, target):
        queue = deque([(list(self.start_symbol), [self.start_symbol])])  
        seen = set()

        while queue:
            current, path = queue.popleft()
            current_string = ''.join(current)

            if current_string == target:
                print(f'Target string "{target}" generated.')
                self.print_path(path)
                return True

            if current_string in seen:
                continue
            seen.add(current_string)

            for i in range(len(current)):
                symbol = current[i]
                if symbol in self.non_terminals:
                    prods = self.productions.get(symbol, [])
                    for prod in prods:
                        new_current = current[:]
                        new_current[i:i+1] = list(prod)
                        new_path = path + [''.join(new_current)]
                        queue.append((new_current, new_path))

        print(f'Target string "{target}" cannot be generated.')
        return False

    def print_path(self, path):
        print(path[0])  
        for step in path[1:]:  
            print(" -> " + step)

def main():
    non_terminals = input('Enter non-terminals (comma separated): ').strip().split(',')
    terminals = input('Enter terminals (comma separated): ').strip().split(',')
    productions = {}
    print('Enter productions (format: A -> a|b|c...d, enter "end" to finish): ')
    while True:
        production_input = input().strip()
        if production_input.lower() == 'end':
            break
        if '->' not in production_input:
            print("Invalid production format. Use 'A -> a|b|c...d'.")
            continue
        parts = production_input.split('->')
        if len(parts) != 2:
            print("Invalid production format. Use 'A -> a|b|c...d'.")
            continue
        non_terminal = parts[0].strip()
        if non_terminal not in non_terminals:
            print(f"Error: {non_terminal} is not a declared non-terminal.")
            continue
        productions[non_terminal] = [prod.strip() for prod in parts[1].split('|')]

    start_symbol = input('Enter start symbol: ').strip()
    if start_symbol not in non_terminals:
        print(f"Error: The start symbol must be one of the non-terminals.")
        return

    target = input('Enter the target string: ').strip()
    cfg = CFG(non_terminals, terminals, productions, start_symbol)
    result = cfg.generate(target)
    print(f'Can the CFG generate the string "{target}"? {result}')

if __name__ == '__main__':
    main()
