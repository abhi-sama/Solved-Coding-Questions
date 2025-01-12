int countingValleys(int steps, string path) {
int count=0;
int valley=0;
for(char c:path)
   { if(c=='D')
        count--;
    else 
    {  count++;
        if(count==0)valley++;
    }   
   }
return valley;
}