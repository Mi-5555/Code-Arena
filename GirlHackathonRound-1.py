class Solution:
    def solve (N,S):
        st = []
        ans = 0
        top=-1
        for i in range(len(s)):
            if s[i] == '(':
                st.append(0)
            elif s[i] == ')':
                c_in = st.pop()
                if c_in > 0:
                    count = c_in
                else:
                    count= 1
                if len(st)==0:
                    ans += count
                else: 
                    st[top] += count
        return ans
