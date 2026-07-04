# Last updated: 7/4/2026, 10:44:28 AM
class Solution:
    def readBinaryWatch(self, turnedOn: int):
        result = []
        
        for hour in range(12):        # 0 to 11
            for minute in range(60):  # 0 to 59
                
                # Count number of 1s in binary representation
                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
                    
                    # Format minute with leading zero if needed
                    time = f"{hour}:{minute:02d}"
                    result.append(time)
        
        return result