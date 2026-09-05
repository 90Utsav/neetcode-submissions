
class Solution:




    def get_all_parts(self,s,partitions,output):
        if len(s)==0:
            output.append(partitions.copy()) # Appending a copy of the current partition (corrected)

        for i in range(len(s)):
            string_part=s[0:i+1]

            if string_part==string_part[::-1]:
                partitions.append(string_part)
                self.get_all_parts(s[i+1:],partitions,output)
                partitions.pop()







    def partition(self, s: str) -> List[List[str]]:
        output=[]
        partitions=[]

        self.get_all_parts(s,partitions,output)

        return output