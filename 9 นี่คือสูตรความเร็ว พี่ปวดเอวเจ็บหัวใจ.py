'''นี่คือสูตรความเร็ว พี่ปวดเอวเจ็บหัวใจ'''
def main():
    '''main'''
    distance = float(input())*1852
    times = int(input())/1000
    veloscity = distance/times
    print('อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที'%veloscity)
main()
