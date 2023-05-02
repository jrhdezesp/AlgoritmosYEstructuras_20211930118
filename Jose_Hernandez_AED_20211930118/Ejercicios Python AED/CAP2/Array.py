class Array(object):

 def __init__(self, initialSize): 
    self.__a = [None] * initialSize 
    self.__nItems = 0 
 def __len__(self): 

    return self.__nItems 
 def get(self, n): 

    if 0 <= n and n < self.__nItems: 

        return self.__a[n] 

 def set(self, n, value): 
    if 0 <= n and n < self.__nItems: 

        self.__a[n] = value 

 def insert(self, item): 
    self.__a[self.__nItems] = item 
    self.__nItems += 1 
    
 def find(self, item): 
    for j in range(self.__nItems):
         if self.__a[j] == item: 
            return j 
            return -1 
        
 def search(self, item): 
     return self.get(self.find(item))
 
 def delete(self, item): 
     for j in range(self.__nItems): 
        if self.__a[j] == item: 
         self.__nItems =-1 
         for k in range(j, self.__nItems):
            self.__a[k] = self.__a[k+1] 
        return True 
        return False 
    
 def traverse(self, function=print):
    for j in range(self.__nItems): 
        function(self.__a[j])

#Metodo del ejercicio 2.1
 def getMaxNum(self):
   a=(max(self.__a))
   return a
   
 #Metodo del ejercicio 2.2 

 def deleteMaxNum(self):
   a=(max(self.__a))
   for c in range(self.__nItems): 
      if self.__a[c] == a: 
       self.__nItems -=1
       self.__a[c]= self.__a.append(None)
       
       for c2 in range(c, self.__nItems):
         self.__a[c2] = self.__a[c2+1]

   print("Numero max eliminado")
 #Metodo del ejercicio 2.3
 def deleto(self):
       a=(max(self.__a))
       for co in range(self.__nItems): 
          if self.__a[co] == a: 
           self.__nItems -=1
           self.__a[co]= self.__a.append(None)
           
           for c2 in range(co, self.__nItems):
             self.__a[c2] = self.__a[c2+1]
             for ca in range(c2, self.__nItems):
                v1=self.__a[co]
                v2=self.__a[co+1]
                v3=0
                for c3 in range(co,self.__nItems):
                   if v1>v2:
                       v3=v1
                       v1=v2
                       v2=v3
                       self.__a[co]=v1
                       self.__a[co+1]=v2
                       
                        
                       
       print("Numero max eliminado")  
    
 #metodo ejercicio 2.4
 def removeDupes(self):
    
    unico=[]
    for i in self.__a:
      if i not in unico :
         unico.append(i)
         
    print(unico)
    
   
