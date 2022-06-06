{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9bf1145c-0a86-4017-89b9-c038a0ab5a58",
   "metadata": {},
   "outputs": [],
   "source": [
    "!install sklearn.externals \n",
    "import joblib\n",
    "clf = joblib.load(\"model.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57126bdb-7e89-4a4c-9bb9-64acd7e55c55",
   "metadata": {},
   "outputs": [],
   "source": [
    "def n(x, xmin, xmax):\n",
    "    nx = x\n",
    "    nx = (nx-xmin)/(xmax-xmin)\n",
    "    return nx\n",
    "a=n(int(input('zadaj SepalLengthCm')),4.3 ,7.9)\n",
    "b=n(int(input('zadaj SepalWidthCm')),2.0, 4.4)\n",
    "c=n(int(input('zadaj PetalLengthCm')),1.0 ,6.9)\n",
    "d=n(int(input('zadaj PetalWidthCm')),0.1 ,2.5)\n",
    "\n",
    "v=clf.predict()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
