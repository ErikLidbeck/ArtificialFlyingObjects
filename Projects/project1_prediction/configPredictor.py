from easydict import EasyDict as edict
from DL_labs.utils.classes import Classes
        
def flying_objects_config(fineGrained:bool=False):

    
 
    cfg = edict()
    CLASSIFICATION = Classes(fineGrained)
    cfg.CLASSES = CLASSIFICATION.classes
    cfg.fineGrained = CLASSIFICATION.fineGrained
    cfg.NUM_CLASSES = len(cfg.CLASSES)    # number of classes
    
    cfg.training_data_dir = "../data/FlyingObjectDataset_10K/training"
    cfg.validation_data_dir = "../data/FlyingObjectDataset_10K/validation"
    cfg.testing_data_dir = "../data/FlyingObjectDataset_10K/testing"

    cfg.GPU = -1                 # GPU ID or set as -1 in case of using any GPU
    cfg.IMAGE_WIDTH = 128       # image width
    cfg.IMAGE_HEIGHT = 128      # image height
    cfg.IMAGE_CHANNEL = 3       # image channel
    cfg.NUM_WORKERS = 4
    cfg.BATCH_SIZE = 32         # batch size
    cfg.SAVE_EVERY = 1         # save after each epoch
    cfg.TENSORBORD_DIR = "logs/"
    #cfg.DATA_AUGMENTATION = True   # Whether to do data augmentation

    return cfg
