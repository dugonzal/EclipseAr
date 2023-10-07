# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dugonzal <dugonzal@student.42urduliz.com>  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/07 12:17:49 by Dugonzal          #+#    #+#              #
#    Updated: 2023/10/07 12:26:47 by Dugonzal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

if __name__ == "__main__":
    run("app:app", host="127.0.0.1", port=8000, reload=True)

