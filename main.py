import ray
from algorithms.sac import SAC


if __name__ == '__main__':
    ray.init(log_to_driver=True)
    sac = SAC()
    sac.logger.log(sac.logger.parameter)
    sac.run()
    #this is a comment
    print("this is a comment")