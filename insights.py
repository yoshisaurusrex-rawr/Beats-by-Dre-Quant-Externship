np.savetxt('cleaned_beats.csv', np.column_stack((ratings, review_len)), delimiter=",", fmt='%s', header="Rating,Review Length")
