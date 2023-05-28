# ================== Likes Vs Dislikes ==================
# Like, Dislike, Nothing come from Preloaded
def like_or_dislike(lst):
    state = "Nothing"
    for button in lst:
        if button == "Like":
            if state == "Dislike":
                state = "Like"
            elif state == "Like":
                state = "Nothing"
            else:
                state = "Like"
        elif button == "Dislike":
            if state == "Like":
                state = "Dislike"
            elif state == "Dislike":
                state = "Nothing"
            else:
                state = "Dislike"
    return state
            