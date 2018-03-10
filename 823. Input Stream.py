class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        # Write your code here
        inputA = list(inputA)
        inputB = list(inputB)
        a=[]
        b=[]
        for i in inputA:
            if i == '<':
                if a:
                    a.pop()
            else:
                a.append(i)
        for j in inputB:
            if j == '<':
                if b:
                    b.pop()
            else:
                b.append(j)
        inputA=''.join(a)
        inputB=''.join(b)
        print inputA,inputB
        if inputA == inputB:
            return 'YES'
        else:
            return 'NO'
