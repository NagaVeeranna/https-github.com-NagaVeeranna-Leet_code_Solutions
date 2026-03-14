class Solution {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        
        int[][] result = new int[rows * cols][2];
        int index = 0;
        
        int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}}; // E, S, W, N
        
        int steps = 1;
        int d = 0;
        
        result[index++] = new int[]{rStart, cStart};
        
        while(index < rows * cols){
            
            for(int i = 0; i < 2; i++){
                
                for(int j = 0; j < steps; j++){
                    
                    rStart += dir[d][0];
                    cStart += dir[d][1];
                    
                    if(rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols){
                        result[index++] = new int[]{rStart, cStart};
                        if(index == rows * cols) return result;
                    }
                }
                
                d = (d + 1) % 4;
            }
            
            steps++;
        }
        
        return result;
    }
}