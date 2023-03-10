class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):

        try:
            if type(entry.title) == str:
                self.entry_list.append(entry)
        except:
            raise Exception("Cannot add non-entries to diary!")

    def all(self):
        
        if self.entry_list == []:
            raise Exception("No entries!")
        
        return (self.entry_list)

    def count_words(self):

        if self.entry_list == []:
            raise Exception("No entries!")
        
        count = 0

        for i in self.entry_list:
            count += i.count_words()

        return count

    def reading_time(self, wpm):

        if self.entry_list == []:
            raise Exception("No entries!")
        
        words_quant = self.count_words()

        return words_quant / wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):

        if self.entry_list == []:  #Check if no entries in the diary
            raise Exception("No entries!")


        number_words_i_can_read = (wpm * minutes)  #check how many words we want to be returned

        correct_entry = None #base correct entry as none

        #find the entry with words closesst (above or below) to the number of words user can read

        for i in self.entry_list:

            if correct_entry == None:
                correct_entry = i
            else:

                distance_to_words_i_can_read = abs(number_words_i_can_read - i.count_words())

                distance_to_words_closest_can_read = abs(number_words_i_can_read - correct_entry.count_words())

                if distance_to_words_i_can_read < distance_to_words_closest_can_read:

                    correct_entry = i


        #correct_entry is the closest to user read

        words_to_read = correct_entry.contents #variable is populated with the string of contents - all words

        words_to_read_list = words_to_read.split() #gets all the words in a list

        words_output_list = [] # makes an empty list

        if len(words_to_read_list) == number_words_i_can_read:
            
            return correct_entry.contents

        elif len(words_to_read_list) < number_words_i_can_read:

            while len(words_output_list) < number_words_i_can_read:
                if len(words_to_read_list) > 0:
                    words_output_list.append(words_to_read_list[0])
                    words_to_read_list.pop(0)
                else:
                    words_to_read = correct_entry.contents
                    words_to_read_list = words_to_read.split()
        
            words_output = " ".join(words_output_list)

            return words_output

        else:
            
            for i in range(number_words_i_can_read):
                words_output_list.append(words_to_read_list[i])
            
            words_output = " ".join(words_output_list)

            return words_output
