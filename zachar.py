def myevald(f, d):
    if type(f)==int:
    	return f
    if type(f)==str:
    	return d.get(f)
    if type(f)==list:
    	a=myevald(f[1],d)
    	b=myevald(f[2],d)
    	if f[0]== '+':
    		return (a+b)
    	if f[0]== '-':
    		return (a-b)
    	if f[0]== '*':
    		return (a*b)
    	if f[0]== '/':
    		return (a/b)

def myderive(f, var):
    if type(f)==int:
    	return 0
    if type(f)==str:
    	if f==var:
    		return 1
    	else:
    		return 0
    if type(f)==list:
    	c1=f[1]
    	c2=f[2]
    	k1=var[0]
    	k2=var[1]
    	if f[0]=="+":
    		if type(c1)==int and type(c2)==int:
    			return ['+',0,0]
    		if type(c1)==int and type(c2)==str:
    			if c2==k1 or c2==k2:
    				return ['+',0,1]
    		if type(c1)==str and type(c2)==int:
    			if c1==k1 or c1==k2:
    				return['+',1,0]			
    	if f[0]=="-":
    		if type(c1)==int and type(c2)==int:
    			return ['-',0,0]
    	if f[0]=="/":
    		if type(c1)==int and type(c2)==int:
    			return ['/',0,0]
    	if f[0]=="*":
    		if type(c1)==int and type(c2)==int:
    			return ['*',0,0]			
    						
    	
    			


    		
