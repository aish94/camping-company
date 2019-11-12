from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from datetime import date
from app.utils import invoice_message_camp
import os
import datetime

from destination.models import (Destination, Map,
                                Region, Amenity, Activity,
                                Detail, Circuit, Booking,
                                Experience, Feature,
                                PaymentCampsite, Pricing)

# Create your views here.


def destination(request):
    list1 = []
    maps = os.environ.get("maps")
    places = Map.objects.all().order_by("pk")
    if request.is_ajax():
        place = request.POST.get("place")
        region = Region.objects.filter(name__icontains=place)

        for x in region:
            for y in x.region.all():
                list1.append(y.pk)
        data = {"list1": list1}
        return JsonResponse(data)

    return render(request, "destination/destination.html", {"places": places, "maps": maps, "list1": list1})


def destination_detail_page(request, slug):
    # Search.objects.new_or_get(request)
    destination = Destination.objects.get(slug=slug)
    activity = Activity.objects.get(destination=destination)
    detail = Detail.objects.get(destination=destination)
    amenity = Amenity.objects.get(destination=destination)
    experience = Experience.objects.filter(destination=destination)
    feature = Feature.objects.get(destination=destination)
    pricing = Pricing.objects.get(destination=destination)
    place = destination.place
    place = 'kdestinationk' + place
    place = place.replace(" ", "-")
    context = {
            "experience": experience,
            "destination": destination,
            "amenity": amenity,
            "activity": activity,
            "detail": detail,
            "place": place,
            "feature": feature,
            "pricing": pricing
           }

    if request.is_ajax():
        if request.user.is_authenticated:
            days = int(request.POST.get("number"))
            caravan = int(request.POST.get("Caravan"))
            ground = int(request.POST.get("Ground"))
            rooftop = int(request.POST.get("Rooftop"))
            dates = datetime.datetime.strptime(request.POST.get("date"), "%Y-%m-%d").date()
            amount = caravan + ground + rooftop
            igst = amount*.18
            convenient = amount*.024
            amount += igst + convenient
            Booking(destination=detail, user=request.user,
                    caravan=caravan, ground=ground, rooftop=rooftop,
                    days=days, date=dates, amount=amount, igst=igst,
                    convenient=convenient).save()
            return JsonResponse({"amount": amount, "email": request.user.email,
                                 "name": request.user.first_name,
                                 "razor_id": os.environ.get("razor_id")
                                 })
        else:
            return redirect("register:signup")

    return render(request, "destination/detail.html", context)


def circuits(request):
    return render(request, "destination/circuits.html")


def circuit(request, slug):
    cir = Circuit.objects.get(slug=slug)
    return render(request, "destination/circuit.html", {"cir": cir})


def success(request):
    now = date.today().strftime("%Y-%m-%d")
    try:
        book = Booking.objects.filter(user=request.user).last()
    except:
        messages.warning(request, "Book a campsite first")
        return redirect("app:home")
    if request.is_ajax():
        txnid = request.POST.get("txnid")
        book.txnid = txnid
        book.save()
        duration = book.days
        caravan = book.caravan
        ground = book.ground
        rooftop = book.rooftop
        txnid = book.txnid
        total = book.amount
        count = book.pk
        email = book.user.email
        name = book.user.first_name
        igst = book.igst
        convenient = book.convenient
        invoice_message_camp(email,  os.environ.get("email"),
                             txnid=txnid, now=now, name=name, convenient=convenient, total=total, duration=duration,
                             count=count, igst=igst, caravan=caravan, ground=ground, rooftop=rooftop)

    return render(request, "destination/success.html", {"book": book})


def camp_add(request):
    maps = os.environ.get("maps")

    if request.is_ajax():
        place = request.GET.get("place")
        destination = Destination.objects.filter(place=place)
        if destination.count() == 1:
            return JsonResponse({"exist": "site already exist"})

    if request.method == "POST":
        # overview section save
        place = request.POST.get("place")
        state_city = request.POST.get("state-city")
        lat = request.POST.get("latitude").split(",")
        latitude = float(lat[0])
        longitude = float(lat[1])
        site_type = request.POST.get("site_type")
        site_description = request.POST.get("site_description")
        image_main = request.FILES["image-main"]
        accessible_by = request.POST.get("accessible_by")
        off_roading = request.POST.get("off_roading")
        cycling = request.POST.get("cycling")
        campfire = request.POST.get("campfire")
        toilet = request.POST.get("toilet")
        known_for = request.POST.get("known_for")
        region = (request.POST.get("region")).lower()

        barbeque = request.POST.get("barbeque")
        kitchen = request.POST.get("kitchen")
        picnic = request.POST.get("picnic")
        drinking = request.POST.get("drinking")
        charging = request.POST.get("charging")
        pets = request.POST.get("pets")
        bathroom = request.POST.get("bathroom")
        covered = request.POST.get("covered")
        breakfast = request.POST.get("breakfast")

        season = request.POST.get("season")
        summer = request.POST.get("summer")
        winter = request.POST.get("winter")

        cave = request.POST.get("cave")
        waterfall = request.POST.get("waterfall")
        trekking = request.POST.get("trekking")
        river = request.POST.get("river_beach")
        swimming = request.POST.get("swimming")
        historical = request.POST.get("historical_place")
        fishing = request.POST.get("fishing")
        farming = request.POST.get("farming")
        lake = request.POST.get("lake")
        boating = request.POST.get("boating")

        bank_name = request.POST.get("bank_name")
        account_number = request.POST.get("account_number")
        IFSC = request.POST.get("IFSC")
        number = request.POST.get("phone")

        caravan = float(request.POST.get("caravan"))
        rooftop = float(request.POST.get("rooftop"))
        BYOT = float(request.POST.get("BYOT"))
        room = float(request.POST.get("room"))
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        cancellation = request.POST.get("cancel")
        book = True
        if caravan == 0 and rooftop == 0 and room == 0 and BYOT == 0:
            book = False

        # creating main foreign key
        try:
            destination = Destination.objects.create(place=place, state_city=state_city, site_type=site_type,
                                                     image_main=image_main, distance=12, hours=12, season=season,
                                                     night_time_temperature_summer=summer, description=site_description,
                                                     night_time_temperature_winter=winter, known_for=known_for)
        except:
            messages.warning(request, "Camp site with same name already taken")
            return redirect("destination:destinations")

        ma = Map.objects.create(destination=destination, latitude=latitude, longitude=longitude,
                                title=place, description=site_description, images=image_main)
        # image title description
        # Description section save
        Detail(destination=destination, accessible_By=accessible_by,check_in=check_in, check_out=check_out,
               cancellation_policy=cancellation).save()
        # crazy for loop
        for x in range(1, 4):
            title = "experience_title" + "-" + str(x)
            description = "experience_description" + "-" + str(x)
            image = "experience_image" + "-" + str(x)
            title = request.POST.get(title)
            description = request.POST.get(description)
            image = request.FILES[image]
            Experience(destination=destination, title=title,
                       description=description, image=image).save()

        Feature(destination=destination, off_roading=off_roading, campfire=campfire,
                cycling=cycling, toilet=toilet).save()

        Amenity(destination=destination, basic_toilet=toilet,barbeque_grills=barbeque,kitchen=kitchen,
                picnic_table=picnic, drinking_water=drinking, charging_points=charging, pets_allowed=pets,
                bathroom=bathroom, campfire=campfire, covered_area=covered, breakfast=breakfast).save()

        Activity(destination=destination, picnic=picnic, off_roading=off_roading, river_beach=river, caving=cave,
                 waterfall=waterfall, trekking=trekking,swimming=swimming, historical_monument=historical,
                 fishing=fishing, local_farm=farming, lake=lake, boating=boating).save()

        PaymentCampsite(destination=destination, user=request.user, bank=bank_name, account=account_number,
                        IFSC=IFSC, phone=number).save()

        Pricing(destination=destination, caravan=caravan, rooftop=rooftop, BYOT=BYOT, room=room, book=book).save()

        reg = Region.objects.filter(name=region)
        if reg.count() == 0:
            reg = Region.objects.create(name=region)
            reg.region.add(ma)
        else:
            reg[0].region.add(ma)
        messages.success(request, "Camp site add success")
        return redirect("destination:destinations")

    return render(request, "destination/camp_add.html", {"maps": maps})


def camp_update(request, slug):
    maps = os.environ.get("maps")
    destination = Destination.objects.get(slug=slug)
    amenity = Amenity.objects.get(destination=destination)
    detail = Detail.objects.get(destination=destination)
    pricing = Pricing.objects.get(destination=destination)
    activity = Activity.objects.get(destination=destination)
    payment = PaymentCampsite.objects.get(destination=destination)
    feature = Feature.objects.get(destination=destination)
    experience = Experience.objects.filter(destination=destination)
    experience1 = experience[0]
    experience2 = experience[1]
    experience3 = experience[2]
    map = Map.objects.get(destination=destination)
    reg = region = Region.objects.get(region=map)
    context = {
        "destination":destination,
        "maps": maps,
        "amenity": amenity,
        "detail": detail,
        "pricing": pricing,
        "feature": feature,
        "activity": activity,
        "payment": payment,
        "map": map,
        "experience1": experience1,
        "experience2": experience2,
        "experience3": experience3,
        "region": region,

    }
    if request.method == "POST":
        # overview section save
        place = request.POST.get("place")
        state_city = request.POST.get("state-city")
        lat = request.POST.get("latitude").split(",")
        latitude = float(lat[0])
        longitude = float(lat[1])
        site_type = request.POST.get("site_type")
        site_description = request.POST.get("site_description")
        try:
            image_main = request.FILES["image-main"]
            no_image = True
        except:
            no_image = False
        accessible_by = request.POST.get("accessible_by")
        off_roading = request.POST.get("off_roading")
        cycling = request.POST.get("cycling")
        campfire = request.POST.get("campfire")
        toilet = request.POST.get("toilet")
        known_for = request.POST.get("known_for")
        region = (request.POST.get("region")).lower()

        barbeque = request.POST.get("barbeque")
        kitchen = request.POST.get("kitchen")
        picnic = request.POST.get("picnic")
        drinking = request.POST.get("drinking")
        charging = request.POST.get("charging")
        pets = request.POST.get("pets")
        bathroom = request.POST.get("bathroom")
        covered = request.POST.get("covered")
        breakfast = request.POST.get("breakfast")

        season = request.POST.get("season")
        summer = request.POST.get("summer")
        winter = request.POST.get("winter")

        cave = request.POST.get("cave")
        waterfall = request.POST.get("waterfall")
        trekking = request.POST.get("trekking")
        river = request.POST.get("river_beach")
        swimming = request.POST.get("swimming")
        historical = request.POST.get("historical_place")
        fishing = request.POST.get("fishing")
        farming = request.POST.get("farming")
        lake = request.POST.get("lake")
        boating = request.POST.get("boating")

        bank_name = request.POST.get("bank_name")
        account_number = request.POST.get("account_number")
        IFSC = request.POST.get("IFSC")

        caravan = float(request.POST.get("caravan"))
        rooftop = float(request.POST.get("rooftop"))
        BYOT = float(request.POST.get("BYOT"))
        room = float(request.POST.get("room"))
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        cancellation = request.POST.get("cancel")
        book = True
        if caravan == 0 and rooftop == 0 and room == 0 and BYOT == 0:
            book = False

        # creating main foreign key
        des = Destination.objects.filter(slug=slug)
        destination = des[0]
        if no_image:
            destination.image_main = image_main
            destination.save()
            des.update(place=place, state_city=state_city, site_type=site_type, distance=12, hours=12, season=season,
                       night_time_temperature_summer=summer, description=site_description,
                       night_time_temperature_winter=winter, known_for=known_for)
        else:
            des.update(place=place, state_city=state_city, site_type=site_type,
                       distance=12, hours=12, season=season,
                       night_time_temperature_summer=summer, description=site_description,
                       night_time_temperature_winter=winter, known_for=known_for)
        if no_image:
            ma = Map.objects.filter(destination=destination)
            m = ma[0]
            m.images = image_main
            m.save()
            ma.update(latitude=latitude, longitude=longitude,
                      title=place, description=site_description)
        else:
            Map.objects.filter(destination=destination).update(latitude=latitude, longitude=longitude,
                                                               title=place, description=site_description)

        # image title description
        # Description section save

        Detail.objects.filter(destination=destination).update(accessible_By=accessible_by,
                                                              check_in=check_in, check_out=check_out,
                                                              cancellation_policy=cancellation)
        # crazy for loop
        for x in range(1, 4):
            title = "experience_title" + "-" + str(x)
            description = "experience_description" + "-" + str(x)
            image = "experience_image" + "-" + str(x)
            title = request.POST.get(title)
            description = request.POST.get(description)
            try:
                image = request.FILES[image]
                expr_image = True
            except:
                expr_image = False

            if expr_image:
                ex = Experience.objects.filter(destination=destination)[x-1]
                ex.title = title
                ex.description = description
                ex.image = image
                ex.save()
            else:
                ex = Experience.objects.filter(destination=destination)[x - 1]
                ex.title = title
                ex.description = description
                ex.save()

        Feature.objects.filter(destination=destination).update(off_roading=off_roading, campfire=campfire,
                                                               cycling=cycling, toilet=toilet)

        Amenity.objects.filter(destination=destination).update(basic_toilet=toilet, barbeque_grills=barbeque,
                                                               kitchen=kitchen,picnic_table=picnic,
                                                               drinking_water=drinking, charging_points=charging,
                                                               pets_allowed=pets,bathroom=bathroom, campfire=campfire,
                                                               covered_area=covered, breakfast=breakfast)

        Activity.objects.filter(destination=destination).update(picnic=picnic, off_roading=off_roading,
                                                                river_beach=river, caving=cave,
                                                                waterfall=waterfall, trekking=trekking,swimming=swimming
                                                                , historical_monument=historical,
                                                                fishing=fishing, local_farm=farming, lake=lake,
                                                                boating=boating)

        PaymentCampsite.objects.filter(destination=destination).update(user=request.user, bank=bank_name,
                                                                       account=account_number, IFSC=IFSC)

        Pricing.objects.filter(destination=destination).update(caravan=caravan, rooftop=rooftop, BYOT=BYOT, room=room,
                                                               book=book)
        reg.region.remove(map)
        reg = Region.objects.filter(name=region)
        if reg.count() == 0:
            reg = Region.objects.create(name=region)
            reg.region.add(map)
        else:
            reg[0].region.add(map)
        messages.success(request, "Camp site update success")
        return redirect("destination:destinations")

    return render(request, "destination/camp_update.html", context)


# def camp_remove(request, slug):
#     return render(request, "destination/camp_update.html")

