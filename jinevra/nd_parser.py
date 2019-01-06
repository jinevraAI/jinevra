

def narrative_dialog(text_as_tokenized_list, quotation_mark_chars):
    # check if text is tokenized
    if isinstance(text_as_tokenized_list, list):
        results = {
            'dialog': [],
            'narrative': []
        }

        current = []
        length = len(text_as_tokenized_list)
        found_q = False
        counter = 0


        while counter < length:
            word = text_as_tokenized_list[counter]
            if word not in quotation_mark_chars:
                current.append(word)

            else:
                if len(current) > 0:
                    results['narrative'].append(current)
                current = []
                current.append(word)
                found_q = True


                while found_q and counter < length-1:
                    counter += 1
                    if text_as_tokenized_list[counter] not in quotation_mark_chars:
                        current.append(text_as_tokenized_list[counter])
                    else:
                        current.append(text_as_tokenized_list[counter])
                        if len(current) > 0:
                            results['dialog'].append(current)
                            current = []
                        found_q = False

            counter += 1

        return (results)

    else:
        print('You need to convert your text to a tokenized list before using this function.')
