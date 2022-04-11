class TrainRace:
    
    
    def __init__(self, lengths, velocities):
        """ Initializes the class with two lists holding the lengths and velocities of trains

            - if list lengths mismatches, raise ValueError
            - if a length or a velocity is less than one, raises ValueError
            
            - MUST execute in O(n) where n is sum of train lengths
            - HINT: think about additional fields which may help speeding up the program
        """
        raise Exception('TODO IMPLEMENT ME !')


    def get_paths(self):
        """ 
            Return the train paths as a list of list of characters
        
            ********  MUST RUN IN O(1)  *********
        
            HAVE YOU READ THE REQUIREMENT ABOVE ?
        """
        raise Exception('TODO IMPLEMENT ME !')


    def step(self):
        """ Steps the simulation by moving each train toward right 
            by a number of cells given by its velocity.            
            
                        
            *** MUST run in O(v) where v is the sum of all velocities     
            
            *** Complexity MUST *NOT* depend on train length nor dashes length
            
            *** For simplicity, ASSUME velocity is always 
                less or equal than train length                 
            
            ********      HAVE YOU READ THE REQUIREMENTS ABOVE ?   ********
        """
        raise Exception('TODO IMPLEMENT ME !')