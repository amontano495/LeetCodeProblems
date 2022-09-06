class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        a,b = 0,0
        rowPos = 0
        if numRows == 1:
            return rows
        else:
            rows.append([1,1])
            rowPos = 1
            while(len(rows) < numRows):
                newRow = []
                oldRow = rows[rowPos]
                newRow.append(1)
                a,b = 0,1
                while(len(newRow) < len(oldRow)):
                    newRow.append(oldRow[a] + oldRow[b])
                    a += 1
                    b += 1
                newRow.append(1)
                rows.append(newRow)
                rowPos += 1
        
        return rows