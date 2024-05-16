
class Score():
    def __init__(self):
        """
        Contains high score variable
        args: None
        return: None
        """
        self.high_score = 0

    def read_score(self):
        """
        Takes high score variable and appends it to
        score text file
        args: None
        return: (String) high_score as string
        """
        score = open("etc/score")
        scores = score.readlines()
        for line in scores:
            if int(line) > self.high_score:
                self.high_score = int(line)
        score.close
        return(str(self.high_score))
    
    def update_score(self, newest_score):
        """
        Takes new score and appends it to
        score text file
        args: (Int) newest score from when snake
        collides and game ends 
        return: None
        """
        score = open("etc/score", "a")
        new_score = str(newest_score)+"\n"
        score.write(new_score)
        score.close
