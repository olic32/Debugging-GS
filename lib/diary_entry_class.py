class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_to_read = []




    def count_words(self):
        
        new_str = self.contents.strip()

        in_word = 0

        count = 0

        for i in new_str:
            if i != " ":
                if in_word == 0:
                    count += 1
                    in_word = 1
            else:
                if in_word == 1:
                    in_word = 0

        return count



    def reading_time(self, wpm):

        return (self.count_words() / wpm)




    def reading_chunk(self, wpm, minutes):

        word_quant = (wpm * minutes)

        words_read_list = self.words_to_read

        words_output_list = []

        while len(words_output_list) < word_quant:
            if len(words_read_list) > 0:
                words_output_list.append(words_read_list[0])
                words_read_list.pop(0)
            else:
                self.words_to_read = self.contents.split()
                words_read_list = self.words_to_read

        words_output = " ".join(words_output_list)

        return words_output









