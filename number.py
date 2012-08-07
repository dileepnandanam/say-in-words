class numbertostring:

	def __init__(self):
		self.name={
			'0':'zero',
			'1':'one',
			'2':'two',
			'3':'three',
			'4':'four',
			'5':'five',
			'6':'six',
			'7':'seven',
			'8':'eight',
			'9':'nine',
			'10':'ten',
			'11':'eleven',
			'12':'twelve',
			'13':'thirteen',
			'14':'fourteen',
			'15':'fifteen',
			'16':'sixteen',
			'17':'seventeen',
			'18':'eighteen',
			'19':'nineteen',
			'20':'twenty',
			'30':'thirty',
			'40':'fourty',
			'50':'fifty',
			'60':'sixty',
			'70':'seventy',
			'80':'eighty',
			'90':'ninety',
			'100':'hundred'
			}
		self.tens={
			
			4:'thousand',
			6:'lakh',
			8:'crore',
			10:'billion',
			13:'trillion',
			16:'quadrillion',
			19:'quintillion',
			22:'sextillion',
			25:'septillion',
			28:'octillion',
			31:'nonillion',
			34:'decillion',
			37:'undecillion',
			40:'duodecillion',
			43:'tredecillion',
			46:'quattuordecillion',
			49:'quindecillion',
			52:'sexdecillion',
			55:'septendecillion',
			58:'octodecillion',
			61:'novemdecillion',
			64:'vigintillion',
			67:'unvigintillion',
			70:'duovigintillion',
			73:'trevigintillion',
			76:'quattuorvigintillion',
			79:'quinvigintillion',
			82:'sexvigintillion',
			85:'septenvigintillion',
			88:'octovigintillio',
			91:'novemvigintillion',
			94:'trigintillion',
			97:'untrigintillion',
			100:'duotrigintillion',
			101:'googol',#10^100
			}
		
		self.namedpowers=[3,4,6,8,10,13,16,19,22,25]
	
		
	
	
	def spelunit(self,n):
		
		if n in self.name.keys():
			
			return self.name[n]
		elif len(n) in self.tens.keys():
			return self.tens[len(n)]

		elif len(n)==2:
			
			return  self.name[n[0]+'0']+' '+self.name[n[1]]
		elif len(n)==3:
			
			return  self.name[n[0]]+' '+self.name['1'+'0'+'0']+' '+self.spelunit(n[1:])
		else:
			
		
			i=len(n)
			while not i in self.tens.keys():
				i-=1
			return self.spelunit(n[:-1*i])+' '+self.spel('1'+n[-1*i:])

	def adjust(self,s):
		i=0;
		while i<len(s) and s[i]=='0':
			i+=1
		return s[i:]
			
	def order(self,p):
		s='1'
		while p>1:
			s+='0'
			p-=1
		return s
		
	def meaning(self,n):
		exp=[]
		n=n+' '
		l=1
		
		while l<=len(n):
			p=l
			l=l+1
			while not l in self.tens.keys() and l<=len(n):
				l+=1
			if l>p:
				exp.append((self.adjust(n[-1*(l):-1*p]),self.order(p)))
			
			
		exp.reverse()	
		
		return exp

	def spel(self,number):
		wordform=''
		exp=self.meaning(number)
		i=0
		l=len(exp)
		while i<l:	
			t=exp[i]
			if not t[0]=='':
				if i==l-1 :
					wordform+=' '+self.spelunit(t[0])
				
				else:
					wordform+=' '+self.spelunit(t[0])+' '+self.spelunit(t[1])
			i+=1
		return wordform[1:]
		
		
	


