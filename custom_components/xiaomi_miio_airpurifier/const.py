"""Constants of the Xiaomi/ZhiMi AirPurifier component."""

DEFAULT_NAME = "Xiaomi Miio Device"
DEFAULT_RETRIES = 20
DATA_KEY = "fan.xiaomi_miio_airpurifier"
DOMAIN = "xiaomi_miio_airpurifier"
DOMAINS = ["fan"]

CONF_MODEL = "model"
CONF_RETRIES = "retries"

MODEL_AIRPURIFIER_V1 = "zhimi.airpurifier.v1"
MODEL_AIRPURIFIER_V2 = "zhimi.airpurifier.v2"
MODEL_AIRPURIFIER_V3 = "zhimi.airpurifier.v3"
MODEL_AIRPURIFIER_V5 = "zhimi.airpurifier.v5"
MODEL_AIRPURIFIER_PRO = "zhimi.airpurifier.v6"
MODEL_AIRPURIFIER_PRO_V7 = "zhimi.airpurifier.v7"
MODEL_AIRPURIFIER_M1 = "zhimi.airpurifier.m1"
MODEL_AIRPURIFIER_M2 = "zhimi.airpurifier.m2"
MODEL_AIRPURIFIER_MA1 = "zhimi.airpurifier.ma1"
MODEL_AIRPURIFIER_MA2 = "zhimi.airpurifier.ma2"
MODEL_AIRPURIFIER_SA1 = "zhimi.airpurifier.sa1"
MODEL_AIRPURIFIER_SA2 = "zhimi.airpurifier.sa2"
MODEL_AIRPURIFIER_2S = "zhimi.airpurifier.mc1"
MODEL_AIRPURIFIER_2H = "zhimi.airpurifier.mc2"
MODEL_AIRPURIFIER_3 = "zhimi.airpurifier.ma4"
MODEL_AIRPURIFIER_3H = "zhimi.airpurifier.mb3"
MODEL_AIRPURIFIER_ZA1 = "zhimi.airpurifier.za1"
MODEL_AIRPURIFIER_AIRDOG_X3 = "airdog.airpurifier.x3"
MODEL_AIRPURIFIER_AIRDOG_X5 = "airdog.airpurifier.x5"
MODEL_AIRPURIFIER_AIRDOG_X7SM = "airdog.airpurifier.x7sm"

MODEL_AIRHUMIDIFIER_V1 = "zhimi.humidifier.v1"
MODEL_AIRHUMIDIFIER_CA1 = "zhimi.humidifier.ca1"
MODEL_AIRHUMIDIFIER_CA4 = "zhimi.humidifier.ca4"
MODEL_AIRHUMIDIFIER_CB1 = "zhimi.humidifier.cb1"
MODEL_AIRHUMIDIFIER_CB2 = "zhimi.humidifier.cb2"
MODEL_AIRHUMIDIFIER_MJJSQ = "deerma.humidifier.mjjsq"
MODEL_AIRHUMIDIFIER_JSQ = "deerma.humidifier.jsq"
MODEL_AIRHUMIDIFIER_JSQ1 = "deerma.humidifier.jsq1"
MODEL_AIRHUMIDIFIER_JSQ3 = "deerma.humidifier.jsq3"
MODEL_AIRHUMIDIFIER_JSQ5 = "deerma.humidifier.jsq5"
MODEL_AIRHUMIDIFIER_JSQS = "deerma.humidifier.jsqs"
MODEL_AIRHUMIDIFIER_JSQ001 = "shuii.humidifier.jsq001"

MODEL_AIRFRESH_A1 = "dmaker.airfresh.a1"
MODEL_AIRFRESH_VA2 = "zhimi.airfresh.va2"
MODEL_AIRFRESH_VA4 = "zhimi.airfresh.va4"
MODEL_AIRFRESH_T2017 = "dmaker.airfresh.t2017"

MODEL_FAN_V2 = "zhimi.fan.v2"
MODEL_FAN_V3 = "zhimi.fan.v3"
MODEL_FAN_SA1 = "zhimi.fan.sa1"
MODEL_FAN_ZA1 = "zhimi.fan.za1"
MODEL_FAN_ZA3 = "zhimi.fan.za3"
MODEL_FAN_ZA4 = "zhimi.fan.za4"
MODEL_FAN_P5 = "dmaker.fan.p5"
MODEL_FAN_P8 = "dmaker.fan.p8"
MODEL_FAN_P9 = "dmaker.fan.p9"
MODEL_FAN_P10 = "dmaker.fan.p10"
MODEL_FAN_P11 = "dmaker.fan.p11"
MODEL_FAN_LESHOW_SS4 = "leshow.fan.ss4"
MODEL_FAN_1C = "dmaker.fan.1c"
MODEL_FAN_FA1 = "zhimi.fan.fa1"
MODEL_FAN_FB1 = "zhimi.fan.fb1"

MODEL_MOSQ_DAKUO = "ateai.mosq.dakuo"

AUTO_DETECT = "auto.detect"
OPT_MODEL = {
    AUTO_DETECT: "Auto Detect",
    MODEL_AIRPURIFIER_V1: "Air Purifier",
    MODEL_AIRPURIFIER_V2: "Air Purifier 2",
    MODEL_AIRPURIFIER_V3: "Air Purifier V3",
    MODEL_AIRPURIFIER_V5: "Air Purifier V5",
    MODEL_AIRPURIFIER_PRO: "Air Purifier Pro",
    MODEL_AIRPURIFIER_PRO_V7: "Air Purifier Pro V7",
    MODEL_AIRPURIFIER_M1: "Air Purifier 2 (mini)",
    MODEL_AIRPURIFIER_M2: "Air Purifier (mini)",
    MODEL_AIRPURIFIER_MA1: "Air Purifier MA1",
    MODEL_AIRPURIFIER_MA2: "Air Purifier MA2",
    MODEL_AIRPURIFIER_SA1: "Air Purifier Super",
    MODEL_AIRPURIFIER_SA2: "Air Purifier Super 2",
    MODEL_AIRPURIFIER_2S: "Air Purifier 2S",
    MODEL_AIRPURIFIER_2H: "Air Purifier 2H",
    MODEL_AIRPURIFIER_3: "Air Purifier 3 (2019)",
    MODEL_AIRPURIFIER_3H: "Air Purifier 3H (2019)",
    MODEL_AIRPURIFIER_ZA1: "Air Purifier ZA1",
    MODEL_AIRPURIFIER_AIRDOG_X3: "Air Dog X3",
    MODEL_AIRPURIFIER_AIRDOG_X5: "Air Dog X5",
    MODEL_AIRPURIFIER_AIRDOG_X7SM: "Air Dog X7SM",
    MODEL_AIRHUMIDIFIER_V1: "Air Humidifier",
    MODEL_AIRHUMIDIFIER_CA1: "Air Humidifier CA1",
    MODEL_AIRHUMIDIFIER_CA4: "Smartmi Humidifier Evaporator 2",
    MODEL_AIRHUMIDIFIER_CB1: "Smartmi Evaporative Humidifier",
    MODEL_AIRHUMIDIFIER_CB2: "Smartmi Evaporative Humidifier",
    MODEL_AIRHUMIDIFIER_MJJSQ: "Mijia Smart Sterilization Humidifier S",
    MODEL_AIRHUMIDIFIER_JSQ: "Mijia Intelligent Sterilization Humidifier",
    MODEL_AIRHUMIDIFIER_JSQ1: "Mijia Intelligent Sterilization Humidifier SCK0A45",
    MODEL_AIRHUMIDIFIER_JSQ3: "Mijia Intelligent Sterilization Humidifier",
    MODEL_AIRHUMIDIFIER_JSQ5: "Mijia Intelligent Sterilization Humidifier",
    MODEL_AIRHUMIDIFIER_JSQS: "Mijia Intelligent Sterilization Humidifier",
    MODEL_AIRHUMIDIFIER_JSQ001: "Zero Fog Humidifier",
    MODEL_AIRFRESH_A1: "Smartmi Fresh Air System",
    MODEL_AIRFRESH_VA2: "Smartmi Fresh Air System (XFXT01ZM)",
    MODEL_AIRFRESH_VA4: "Smartmi Fresh Air System (XFXTDFR02ZM)",
    MODEL_AIRFRESH_T2017: "Mi Fresh Air Ventilator",
    MODEL_FAN_V2: "Pedestal Fan V2",
    MODEL_FAN_V3: "Pedestal Fan V3",
    MODEL_FAN_SA1: "Pedestal Fan SA1",
    MODEL_FAN_ZA1: "Pedestal Fan A1",
    MODEL_FAN_ZA3: "Pedestal Fan ZA3",
    MODEL_FAN_ZA4: "Pedestal Fan ZA4",
    MODEL_FAN_P5: "Pedestal Fan P5",
    MODEL_FAN_P8: "Pedestal Fan P8",
    MODEL_FAN_P9: "Pedestal Fan P9",
    MODEL_FAN_P10: "Pedestal Fan P10",
    MODEL_FAN_P11: "Pedestal Fan P11",
    MODEL_FAN_FA1: "Xiaomi Circulating Fan",
    MODEL_FAN_FB1: "Xiaomi Circulating Fan (Global)",
    MODEL_FAN_LESHOW_SS4: "Rosou SS4 Ventilator",
    MODEL_FAN_1C: "Pedestal Fan Fan 1C",
    MODEL_MOSQ_DAKUO: "Dakoo Mosquito Dispeller"
}

