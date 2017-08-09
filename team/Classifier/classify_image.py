import os

from . import inception


def classify(image_path):

    # Download Inception model if not already done.
    inception.maybe_download()

    # Load the Inception model so it is ready for classifying images.
    model = inception.Inception()

    # Path for a jpeg-image that is included in the downloaded data.
    image_path = os.path.join('team/Classifier/images', image_path + '.jpg')

    # Use the Inception model to classify the image.
    pred = model.classify(image_path=image_path)

    # Print the scores and names for the top-10 predictions.
    scores = model.print_scores(pred=pred, k=10)

    # Close the TensorFlow session.
    model.close()
    return scores

if __name__ == '__main__':
    # Don't include the extension of the image as the image must always be a jpg
    classify("name")
