yCoordinate = random (50, 200)
XCoordinate = random (50, 200)
ySpeed=2
xSpeed=2
ellipseSize= 20



def setup():
    size(600, 800)
        
def draw():
    background(0)
    global XCoordinate, yCoordinate, ySpeed, xSpeed, ellipseSize
    topBoundary = ellipseSize /2
    bottomBoundary = 800 - ellipseSize / 2
    
    leftBoundary = ellipseSize /2
    rightBoundary = 600 - ellipseSize / 2
    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        ySpeed = -ySpeed
        
    if XCoordinate >= rightBoundary or XCoordinate <= leftBoundary:
        xSpeed = -xSpeed
        
    
    yCoordinate = yCoordinate + ySpeed
    XCoordinate += ySpeed
    
    fill (255, 0, 255)
    ellipse(XCoordinate, yCoordinate, ellipseSize, ellipseSize)
    
    
        
    
