def predict_gender_from_volume(total_volume):

    if total_volume < 14500:
        return "Female"
    else:
        return "Male"