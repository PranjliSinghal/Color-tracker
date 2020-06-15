# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:08:05 2019

@author: user
"""

import numpy as np
import cv2

def main():
    cap=cv2.VideoCapture(0)
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
        
    while ret:
        ret,frame=cap.read()
        
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        #blue color (hsv for light blue to dark blue range)
        #low = np.array([100,50,50])
        #high = np.array([140,255,255])
        
        #green color 
        #low = np.array([40,50,50])
        #high = np.array([80,255,255])
        
        #green color
        low = np.array([33,80,40])
        high = np.array([102,255,255])
        
        #masking gives binary image based on range given
        mask=cv2.inRange(hsv,low,high)
        #to show only the green image
        output=cv2.bitwise_and(frame,frame,mask= mask)
        cv2.imshow("Output",output)
        #morphology
        #pening removes randomly popping dots
        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        #closing closes small holes present in actual object
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
            
        #output=cv2.bitwise_and(frame,frame,mask=mask)
        
        maskFinal=maskClose
        conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
        cv2.drawContours(frame,conts,-1,(0,0,255),-1)
        #cv2.imshow("HSV",hsv)     
        cv2.imshow("Video",frame)
        #print(image_mask)
        #cv2.imshow("Mask",mask)
        #cv2.imshow("MaskOpen",maskOpen)
        #cv2.imshow("MaskClose",maskClose)
        '''cv2.imshow("Color tracking",output)'''
        
        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__=="__main__":
    main()