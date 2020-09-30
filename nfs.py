#Interesting number
Given a number 'n', write a program to check if it is a interesting number. 
A interesting number is a number which can be expressed as sum of the digits 
raised to its positional value
 
Input format:
n
 
Output Format:
Yes/No
 
Sample Input:
89
 
Sample Output:
Yes
 
Explanation:
 
8^1+9^2=8+81=89=n. So print 'Yes'



Input
89
Expected output
Yes
-----------
Input
80
Expected output
No
----------------
Input
134
Expected output
No
-----------------
Input
2427
Expected output
Yes







def no_of_digits(n):
    count=0
    while n!=0:
        n//=10
        count+=1
    return count    
n=int(input())
tmp=n
sum=0
N=no_of_digits(n)
while tmp!=0:
    m=tmp%10
    sum=sum+pow(m,N)
    tmp//=10
    N-=1
if sum==n:
    print("Yes")
else:
    print("No")
    
