{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Stock Price ",
      "provenance": [],
      "authorship_tag": "ABX9TyPgr50yTb1RDW6DJe8Kzi+0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Hadeyal/UAS-SUSULAN/blob/main/Stock_Price.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "7_6vFMsaAJNI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "def priceTracker():\n",
        "\n",
        "\n",
        "    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'\n",
        "\n",
        "    response = requests.get(url)\n",
        "    soup = BeautifulSoup(response.text, 'lxml')\n",
        "    #print(soup)\n",
        "    price = soup.find_all('div', {'class' : 'My(6px) Pos(r) smartphone_Mt(6px) W(100%) '})[0].find().text\n",
        "    return price\n",
        "\n",
        "print('Current Price : ' + priceTracker())\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKME7HB-zodB",
        "outputId": "d81d9cc4-ec48-44df-fdf5-2486c0ea898c"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Current Price : 172.39-0.29 (-0.17%)At close:  04:00PM EST172.52 +0.13 (+0.08%)After hours: 07:59PM EST\n"
          ]
        }
      ]
    }
  ]
}