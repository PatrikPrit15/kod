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
   "execution_count": 8,
   "id": "57126bdb-7e89-4a4c-9bb9-64acd7e55c55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "zadaj SepalLengthCm 1\n",
      "zadaj SepalWidthCm 1\n",
      "zadaj PetalLengthCm 1\n",
      "zadaj PetalWidthCm 1\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'builtin_function_or_method' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_5948/3344851494.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[0md\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'zadaj PetalWidthCm'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m0.1\u001b[0m \u001b[1;33m,\u001b[0m\u001b[1;36m2.5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m \u001b[0mv\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mclf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marray\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreshape\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'builtin_function_or_method' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from sklearn.svm import SVC\n",
    "def n(x, xmin, xmax):\n",
    "    nx = x\n",
    "    nx = (nx-xmin)/(xmax-xmin)\n",
    "    return nx\n",
    "a=n(float(input('zadaj SepalLengthCm')),4.3 ,7.9)\n",
    "b=n(float(input('zadaj SepalWidthCm')),2.0, 4.4)\n",
    "c=n(float(input('zadaj PetalLengthCm')),1.0 ,6.9)\n",
    "d=n(float(input('zadaj PetalWidthCm')),0.1 ,2.5)\n",
    "\n",
    "v=clf.predict(np.array[a,b,c,d].reshape(1, -1))"
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
