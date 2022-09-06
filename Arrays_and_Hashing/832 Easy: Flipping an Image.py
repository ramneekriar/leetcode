class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        midpoint = len(image) // 2
        imgLen = len(image)
        
        # horizontal flip
        for img in image:
            for i in range(0, midpoint):
                img[i], img[imgLen - 1 - i] = img[imgLen - 1 - i], img[i]
        
        # invert
        for img in image:
            for i in range(0, imgLen):
                if img[i] == 1:
                    img[i] = 0
                else:
                    img[i] = 1
        return image