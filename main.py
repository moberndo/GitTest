# title
#author: moberndo

if __name__ == '__main__':
    try:
        import numpy as np
    except:
        raise(ImportError('Could not import Numpy.'))
    else:
        print('Numpy successfully imported.')
    print('A new line.')
