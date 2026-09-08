"""
Algoritmo Backtraking para resolver o Problema substes!
"""
def subsets(nums:list[int]):
    n = len(nums)
    result, solution = [], []

    def backtrack(i):
        # Caso Base, define se chegou ao 'fundo' da arvore ou não!
        if i == n:
            result.append(solution[:])
            return

        # Caso de eu ir para esquerda da arvore (n'ao pego valor)
        backtrack(i + 1)

        # Caso de eu pegar valores (andar para direita da arvore)
        solution.append(nums[i])
        backtrack(i + 1)
        solution.pop()

    backtrack(0) # Partindo do 0
    return result

print(subsets([1,2,4,5,7,8]))
        