selected = 0
amount_sorted = 0
done = False

def sort(rectangles, repeat):
    global selected, amount_sorted, done
    selected_rectangle = None

    if done:# Plays end animation
        if selected + 1 < len(rectangles):
            rectangles[selected].select(True)
        selected += 1
        return rectangles


    if selected < len(rectangles):
        rectangles[selected].select()

        if amount_sorted == rectangles[selected].correct_position:# If the rectangle is the correct one
            amount_sorted += 1
            selected_rectangle = selected

        if len(rectangles) > selected + 1:# If the next rectangle is correct, make it blue
            if amount_sorted == rectangles[selected + 1].correct_position:
                rectangles[selected + 1].select(True)        

    selected += 1
    
    if selected > len(rectangles) + 1:# Checks if the sorting is done
        done = True
        selected = 0

    if selected_rectangle != None:# Intserts the rectangle in it's correct position
        rectangles.insert(amount_sorted - 1, rectangles.pop(selected_rectangle))
        selected = amount_sorted - 1

    return rectangles


def reset():
    global selected, amount_sorted, done
    selected = 0
    amount_sorted = 0
    done = False