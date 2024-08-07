from collections import deque

class ContextFreeGrammar:
    def __init__(self, non_terminals, terminals, production_rules, start_symbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.production_rules = production_rules
        self.start_symbol = start_symbol

    def generate_target(self, target_string):
        search_queue = deque([(tuple(self.start_symbol), [self.start_symbol])])
        seen_states = set()

        while search_queue:
            current_state, derivation_path = search_queue.popleft()
            state_string = ''.join(current_state)

            if state_string == target_string:
                print(f'Target string "{target_string}" generated.')
                self.display_derivation_path(derivation_path)
                return True

            if state_string in seen_states:
                continue
            seen_states.add(state_string)

            for index in range(len(current_state)):
                current_symbol = current_state[index]
                if current_symbol in self.non_terminals:
                    possible_productions = self.production_rules.get(current_symbol, [])
                    for production in possible_productions:
                        new_state = list(current_state)
                        new_state[index:index+1] = production.replace(" ", "")
                        new_path = derivation_path + [''.join(new_state)]
                        search_queue.append((tuple(new_state), new_path))

        print(f'Target string "{target_string}" cannot be generated.')
        return False

    def display_derivation_path(self, derivation_path):
        print(derivation_path[0])
        for step in derivation_path[1:]:
            print(" -> " + step)

def main():
    non_terminals = input('Enter non-terminals (comma separated): ').strip().split(',')
    terminals = input('Enter terminals (comma separated): ').strip().split(',')
    production_rules = {}
    print('Enter production rules (format: A -> a|b|c...d, then press enter if done, type "end" to finish): ')
    while True:
        user_input = input().strip()
        if user_input.lower() == 'end':
            break
        if '->' not in user_input:
            print("Invalid production format. Use 'A -> a|b|c...d'.")
            continue
        parts = user_input.split('->')
        if len(parts) != 2:
            print("Invalid production format. Use 'A -> a|b|c...d'.")
            continue
        non_terminal = parts[0].strip()
        if non_terminal not in non_terminals:
            print(f"Error: {non_terminal} is not a declared non-terminal.")
            continue
        production_rules[non_terminal] = [production.strip() for production in parts[1].split('|')]

    start_symbol = input('Enter start symbol: ').strip()
    if start_symbol not in non_terminals:
        print(f"Error: The start symbol must be one of the non-terminals.")
        return

    target_string = input('Enter the target string: ').strip().replace(" ", "")
    cfg = ContextFreeGrammar(non_terminals, terminals, production_rules, start_symbol)
    result = cfg.generate_target(target_string)
    print(f'Can the CFG generate the string "{target_string}"?\n{result}')

if __name__ == '__main__':
    main()
